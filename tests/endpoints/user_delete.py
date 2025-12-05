import requests

from tests.endpoints.endpoint import Endpoint


class DeleteUser(Endpoint):
    """
    Endpoint test helper for deleting a user via /users/{user_id}.

    Provides methods to send DELETE requests and validate deletion responses.
    Inherits common functionality from the base Endpoint class.
    """

    def delete_user_by_id(
            self,
            user_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a DELETE request to remove a user by their ID.

        Args:
            user_id (int): The ID of the user to delete.
            headers (dict | None): Optional request headers.
                If not provided, an admin bearer token is added automatically.

        Side Effects:
            - Stores the response object in `self.response`.
            - Stores the parsed response body in `self.body`.
        """
        # If no custom headers provided, use admin token for authorization
        if headers is None:
            headers = self._get_admin_authorization_headers()

        # Send DELETE request to the specified user's endpoint
        self.response = requests.delete(
            url=f"{self.url_users}/{user_id}",
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()

    def check_delete_response_message_is_correct(
            self, user_id: int
    ) -> None:
        """
        Assert that the deletion response contains the correct confirmation
        message.

        Args:
            user_id (int): The ID of the user that was deleted.

        Raises:
            AssertionError: If the actual message does not match the expected.
        """
        expected_message = f"User with ID {user_id} has been deleted."
        actual_message = self.body["message"]
        assert expected_message == actual_message, (
            f"Expected message: {expected_message},"
            f" Actual message: {actual_message}"
        )
