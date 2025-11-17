from tests_async.endpoints.endpoint import Endpoint


class RetrieveAllUsers(Endpoint):
    """
    Endpoint test helper for retrieving all users via GET /users.

    Provides methods to fetch the list of users and verify
    the amount returned in response.
    """

    async def retrieve_all_users(
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

        # If no custom headers provided, use admin token for authorization
        if headers is None:
            headers = await self._get_admin_authorization_headers()

        # Send GET request to retrieve all users
        self.response = await self.client.get(
            url=f"{self.url_users}",
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
        """
        assert self.body is not None, "Response body is None"
        users_in_response = len(self.body)

        assert users_in_response >= created_users, (
            f"Expected at least {created_users} users, but"
            f" received {users_in_response}"
        )
