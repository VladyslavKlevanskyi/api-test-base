import requests
from typing import Any

from tests_sync.endpoints.endpoint import Endpoint


class UpdateUserPass(Endpoint):
    """
    Endpoint test helper for updating a user's password via
    PATCH /users/{user_id}/password.

    Inherits functionality from the base Endpoint class and provides a method
    to send password update requests.
    """

    def update_user_password(
            self,
            user_id: int,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a PATCH request to update a user's password.

        Args:
            user_id (int): ID of the user whose password will be updated.
            headers (dict[str, str] | None): Optional HTTP headers.
                If not provided, an admin bearer token will be used
                automatically.
            payload (dict[str, Any]): Request body containing the new password.
                Example:
                    {"password": "NewStrongPass123!"}

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """
        # Use default admin authorization if headers are not provided
        if headers is None:
            headers = self._get_admin_authorization_headers()

        # Send PATCH request to update the user's password
        self.response = requests.patch(
            url=f"{self.url_users}/{user_id}/password",
            json=payload,
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()
