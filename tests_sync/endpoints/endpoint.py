import os
import dotenv

from datetime import datetime
from typing import Any
from httpx import Response

from tests_sync.auth_tools import get_valid_token

dotenv.load_dotenv()

BASE_URL = os.getenv("BASE_URL")

class Endpoint:
    """
    Base class for API endpoint tests.

    Contains common functionality to test response status codes,
    field types, equality checks, and error messages.
    """
    def __init__(self) -> None:
        """
        Initialize the endpoint helper with a test client and prepare
        auth headers.
        """
        self.url_root: str = BASE_URL
        self.url_apartments: str = BASE_URL + "apartments"
        self.url_users: str = BASE_URL + "users"
        self.response: Response | None = None
        self.body: dict[str, Any] | None = None
        self.apartment_id: int | None = None
        self.unit_id: int | None = None
        self.user_id: int | None = None

        # Prepare authorization header using token from test credentials
        self.headers: dict[str, str] = {
            "Authorization": "Bearer " + get_valid_token(
                base_url=self.url_root,
                username=os.getenv("TEST_USERNAME"),
                password=os.getenv("TEST_PASS")
            )
        }

    def _get_admin_authorization_headers(self) -> dict[str, str]:
        """
        Generate authorization headers using admin credentials.

        This helper method is useful for tests that require admin-level
        access. It retrieves the admin username and password from environment
        variables, obtains a valid token, and constructs the appropriate
        Authorization header.

        Returns:
            dict[str, str]: A dictionary containing the Bearer token in the
                            Authorization header.
        """
        headers = {
            "Authorization": "Bearer " + get_valid_token(
                base_url=self.url_root,
                username=os.getenv("ADMIN_USERNAME"),
                password=os.getenv("ADMIN_PASSWORD")
            )
        }

        return headers

    def check_that_status_is(
            self,
            code: int,
            error_message: str | None = None
    ) -> None:
        """
        Assert that the response status code matches the expected one.

        Args:
            code: Expected HTTP status code.
            error_message: Optional custom message for failure.
        """
        assert self.response is not None, "Response is None"
        
        if error_message is not None:
            assert self.response.status_code == code, error_message
        else:
            assert self.response.status_code == code, (
                f"Expected status code: {code}, "
                f"Actual status code: {self.response.status_code}"
            )

    def check_that_field_type_is(
            self,
            field: str,
            expected_type: type[Any]
    ) -> None:
        """
        Assert that a field exists and has the expected type.

        Args:
            field: Field name.
            expected_type: Expected Python type (e.g., str, int).
        """
        assert self.body is not None, "Response body is None"

        assert field in self.body, (
            f"Field '{field}' not found in response. "
            f"Available fields: {list(self.body.keys())}"
        )

        actual_value = self.body.get(field)
        assert isinstance(actual_value, expected_type), (
            f"Expected field '{field}' "
            f"to be of type '{expected_type.__name__}'"
            f", but got '{type(actual_value).__name__}' "
            f"with value '{actual_value}'"
        )

    def check_that_field_equals(
            self,
            field: str,
            expected_value: str | int | bool
    ) -> None:
        """
        Assert that a field has the expected value.

        Args:
            field: Field name.
            expected_value: Expected value.
        """
        assert self.body is not None, "Response body is None"
        actual = self.body.get(field)
        assert actual == expected_value, (
            f"Expected field '{field}' to be '{expected_value}',"
            f" but got '{actual}'"
        )

    def check_create_and_update_fields(
            self,
            time_tolerance: int,
            field: str,
            expected_value: str
    ) -> None:
        """
        Assert that a field has the expected value.

        Args:
            field: Field name.
            expected_value: Expected value.
            time_tolerance: Acceptable time difference
        """
        assert self.body is not None, "Response body is None"
        actual = self.body.get(field)
        expected_dt = datetime.fromisoformat(
            str(expected_value).replace("Z", "+00:00")
        )
        actual_dt = datetime.fromisoformat(
            str(actual).replace("Z", "+00:00")
        )
        time_difference = abs((actual_dt - expected_dt).total_seconds())
        assert time_difference <= time_tolerance, (
            f"Expected '{field}' to be within {time_tolerance}sec of"
            f" '{expected_dt}', but got '{actual_dt}'"
            f" (difference: {time_difference:.2f}sec)"
        )

    def check_apartment_not_found_message(
            self,
            value: int,
            searching_field: str = "ID"
    ) -> None:
        """
        Assert the correct 'not found' message for an apartment.

        Args:
            value: Value that was searched for (e.g. ID).
            searching_field: Field used for the search (default: "ID").
        """
        assert self.body is not None, "Response body is None"

        expected_message = (
            f"Apartment with {searching_field} {value} not found."
        )
        actual_message = self.body["detail"]
        assert expected_message == actual_message, (
            f"Expected message: {expected_message},"
            f" Actual message: {actual_message}"
        )

    def check_user_not_found_message(
            self, user_id: int
    ) -> None:
        """
        Assert the correct 'not found' message for a user.

        Args:
            user_id: User ID.
        """
        assert self.body is not None, "Response body is None"
        expected_message = f"User with ID {user_id} not found."
        actual_message = self.body["detail"]
        assert expected_message == actual_message,  \
            (f"Expected message: {expected_message},"
             f" Actual message: {actual_message}")

    def check_user_response_body_is_correct(
            self, expected_message: str
    ) -> None:
        """
        Assert the correct error message for user-related request.

        Handles status codes: 400, 401, 403, 422.

        Args:
            expected_message: Expected error message.
        """
        assert self.response is not None, "Response is None"
        assert self.body is not None, "Response body is None"

        if self.response.status_code == 422:
            actual_message = self.body["detail"][0]["msg"]
        elif self.response.status_code in (400, 401, 403):
            actual_message = self.body["detail"]
        else:
            raise AssertionError(
                f"Unexpected status code: {self.response.status_code}"
            )

        assert expected_message == actual_message, (
            f"Expected message: {expected_message},"
            f" Actual message: {actual_message}"
        )

    def check_field_validation_error_response(
            self, expected_error: tuple[str, str]
    ) -> None:
        """
        Assert that field-level validation error matches expected field
        and message.

        Args:
            expected_error: Tuple of (field_name, error_message).
        """
        assert self.body is not None, "Response body is None"
        detail = self.body["detail"][0]

        response_field_name = detail["loc"][1]
        response_msg = detail["msg"]
        expected_field_name, expected_msg = expected_error

        assert response_field_name == expected_field_name, (
            f"Expected field name: {expected_field_name}. "
            f"Actual field name: {response_field_name}"
        )

        assert response_msg == expected_msg, (
            f"Expected message: {expected_msg}. "
            f"Actual message: {response_msg}"
        )
