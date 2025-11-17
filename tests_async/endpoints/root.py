from typing import Any
from tests_async.endpoints.endpoint import Endpoint


class HomePage(Endpoint):
    """
    Async endpoint test helper for the root (home) page.

    Inherits common functionality from the base Endpoint class.
    """
    async def open(self) -> dict[str, Any] | None:
        """
        Send an asynchronous GET request to the root URL ('/').

        Returns:
            Parsed JSON response body if status code is 200,
            otherwise None.
        """
        self.response = await self.client.get(self.url_root)
        if self.response.status_code == 200:
            self.body = self.response.json()
            return self.body

    def check_response_message(self, expected_message: str) -> None:
        """
        Assert that the response body contains the expected 'message' field.

        Args:
            expected_message: The expected message string.

        Raises:
            AssertionError: If the actual message does not match the expected.
        """
        received_message = self.body["message"]
        assert expected_message == received_message, (
            f"Expected message: {expected_message}, "
            f"Actual message: {received_message}"
        )
