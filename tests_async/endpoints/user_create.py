from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class CreateUser(Endpoint):
    """
    Async endpoint test helper for creating a new user via /users/register.

    Inherits from the base async Endpoint class and provides functionality
    to send a user registration request and store the created user ID.

    This class is used in asynchronous test suites and utilizes
    httpx.AsyncClient for making non-blocking HTTP requests.
    """

    async def register_new_user(
            self,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Register a new user by sending an asynchronous POST
        request to /users/register.

        Args:
            payload (dict[str, Any]): Dictionary containing user registration
                data.
            headers (dict[str, str] | None): Optional headers. If not provided,
                an admin bearer token will be automatically generated.

        Side Effects:
            - Saves the full response object in `self.response`.
            - Saves the parsed response body (JSON) in `self.body`.
            - Sets `self.user_id` if the user was successfully created.

        Example payload:
            {
                "username": "test_user",
                "password": "StrongPass123!"
            }
        """
        # If no custom headers provided, use admin token for authorization
        if headers is None:
            headers = await self._get_admin_authorization_headers()

        # Send POST request to register the new user
        self.response = await self.client.post(
            url=f"{self.url_users}/register",
            json=payload,
            headers=headers
        )

        # Parse response JSON body
        self.body = self.response.json()

        # Save user ID if creation was successful (HTTP 201 Created)
        if self.response.status_code == 201:
            self.user_id = self.body["id"]
