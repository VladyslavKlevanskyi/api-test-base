from typing import Any
from tests_async.endpoints.endpoint import Endpoint


class Login(Endpoint):
    """
    Async helper class for handling user authentication via /users/login.

    Inherits from the async base Endpoint class and provides methods to send
    login requests and retrieve bearer tokens.
    """

    async def login(self, payload: dict[str, Any]) -> dict[str, str]:
        """
        Send an async POST request to /users/login to authenticate a user.

        Args:
            payload (dict[str, Any]): Dictionary with login credentials.
                Example:
                    {
                        "username": "test_user",
                        "password": "StrongPass123!"
                    }

        Returns:
            dict[str, str]: A dictionary containing the Authorization header
            with the Bearer token if login is successful.

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """

        # Send POST request to the login endpoint with provided credentials
        self.response = await self.client.post(
            url=f"{self.url_users}/login",
            json=payload,
        )

        # Parse and store JSON response body
        self.body = self.response.json()

        if self.response.status_code == 200:
            access_token = self.body["access_token"]
            return {"Authorization": f"Bearer {access_token}"}
