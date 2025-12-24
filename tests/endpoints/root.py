import allure
import requests

from tests.endpoints.endpoint import Endpoint


class HomePage(Endpoint):
    """
    Endpoint test helper for the root (home) page.
    Inherits common functionality from the base Endpoint class.
    """

    @allure.step("Open home page")
    def open(self) -> None:
        """
        Send a GET request to the root URL.

        Returns:
            dict[str, Any] | None: Parsed JSON response body if status 200,
            otherwise None.
        """

        self.response = requests.get(self.url_root)
        if self.response.status_code == 200:
            self.body = self.response.json()

    @allure.step("Check response message")
    def check_response_message(self, expected_message: str) -> None:
        """
        Assert that the response body contains the expected 'message' field.

        Args:
            expected_message (str): The expected message string.

        Raises:
            AssertionError: If the actual message does not match the expected.
        """
        assert self.body is not None, "Response body is None"
        received_message = self.body["message"]
        assert expected_message == received_message, (
            f"Expected message: {expected_message}, "
            f"Actual message: {received_message}"
        )
