import requests
from typing import Any

from tests_sync.endpoints.endpoint import Endpoint


class Login(Endpoint):
    """
    A class for handling authorization requests.

    Inherits from Endpoint and provides authorization method and verify the
    response.
    """

    def login(self, payload: dict[str, Any]) -> None:
        """
        Send a POST request to /users/login to authenticate a user.

        Args:
            payload (dict[str, Any]): Dictionary with login credentials.
                Example:
                    {
                        "username": "test_user",
                        "password": "StrongPass123!"
                    }

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`
            (if available).
        """
        # Send POST request to the login endpoint with provided credentials
        self.response = requests.post(
            url=f"{self.url_users}/login",
            json=payload,
        )

        # Parse and store JSON response body
        self.body = self.response.json()
