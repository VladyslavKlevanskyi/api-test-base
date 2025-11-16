from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class UpdateUserPass(Endpoint):
    """
    Async endpoint test helper for updating a user's password via
    PATCH /users/{user_id}/password.

    Inherits functionality from the async Endpoint base class and provides
    a method to send password update requests.
    """
    async def update_user_password(
            self,
            user_id: int,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an async PATCH request to update a user's password.

        Args:
            user_id (int): ID of the user whose password will be updated.
            headers (dict[str, str] | None): Optional HTTP headers.
                If not provided, an admin bearer token will be used
                automatically.
            payload (dict[str, Any]): Request body containing the new
                                      password.
                Example:
                    {"password": "NewStrongPass123!"}

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed response body in `self.body`.
        """

        # If no custom headers provided, use admin token for authorization
        if headers is None:
            headers = await self._get_admin_authorization_headers()

        # Send PATCH request to update the user's password
        self.response = await self.client.patch(
            url=f"{self.url_users}/{user_id}/password",
            json=payload,
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()
