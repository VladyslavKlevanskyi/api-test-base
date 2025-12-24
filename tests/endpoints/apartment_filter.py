import allure
import requests
from typing import Any

from tests.endpoints.endpoint import Endpoint


class FilterApartments(Endpoint):
    """
    Endpoint test helper for filtering apartments.

    Provides methods to send POST requests with filters
    and validate the count of returned results.
    """

    @allure.step("Send POST request to /apartments/filter/")
    def retrieve_apartments_by_field_value(
            self,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a POST request to filter apartments based on field values.

        Args:
            payload: Dictionary of filter parameters.
            headers: Optional request headers. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are provided
        if headers is None:
            headers = self.headers

        # Send POST request to /apartments/filter/
        self.response = requests.post(
            url=f"{self.url_apartments}/filter",
            json=payload,
            headers=headers
        )

        # Parse JSON response body
        self.body = self.response.json()

    @allure.step("Check that retrieved apartment count is {count}")
    def check_apartment_count(self, count: int) -> None:
        """
        Assert that the number of returned apartments matches the expected
        count.

        Args:
            count: Expected number of apartment objects in the response.
        """
        assert self.body is not None, "Response body is None"

        apartments_in_response = len(self.body)
        assert apartments_in_response == count, (
            f"Expected {count} objects, but"
            f" received {apartments_in_response}"
        )
