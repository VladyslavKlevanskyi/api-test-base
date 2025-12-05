import requests

from tests.endpoints.endpoint import Endpoint


class RetrieveAllUsers(Endpoint):
    """
    Endpoint test helper for retrieving all users via GET /users.

    Provides methods to fetch the list of users and verify
    the amount returned in response.
    """

    def retrieve_all_users(
            self,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a GET request to retrieve all users.

        Args:
            headers (dict[str, str] | None): Optional HTTP headers.
                If not provided, an admin bearer token is generated
                automatically.

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """
        # Use default admin authorization if no custom headers provided
        if headers is None:
            headers = self._get_admin_authorization_headers()

        # Send GET request to retrieve all users
        self.response = requests.get(
            url=self.url_users,
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()

    def check_retrieved_users_not_less_than_created(
            self,
            created_users: int
    ) -> None:
        """
        Check that the number of users returned is at least
        as many as were just created.

        Args:
            created_users (int): The number of users expected
                to be present in the response (e.g., from a test setup).

        Raises:
            AssertionError: If the number of users in response
                            is less than expected.
            AssertionError: If the response body is None.
        """
        assert self.body is not None, "Response body is None."
        users_in_response = len(self.body)

        assert users_in_response >= created_users, (
            f"Expected at least {created_users} users, but"
            f" received {users_in_response}"
        )
