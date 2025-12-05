import requests

from tests.endpoints.endpoint import Endpoint


class Me(Endpoint):
    """
    Endpoint test helper for accessing the current user's profile
    via /users/me.

    Inherits common functionality from the base Endpoint class and
    provides a method to retrieve authenticated user details.
    """
    def open_me(self, headers: dict[str, str] | None = None) -> None:
        """
        Send a GET request to /users/me to retrieve the current user's data.

        Args:
            headers (dict[str, str] | None): Optional HTTP headers to use
                in the request. If not provided, default authorization headers
                will be used.

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """
        # Use provided headers if available; otherwise, use default headers
        if headers is None:
            headers = self.headers

        # Send GET request to the /users/me endpoint
        self.response = requests.get(
            url=f"{self.url_users}/me",
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()
