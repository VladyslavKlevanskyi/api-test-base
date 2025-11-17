from tests_async.endpoints.endpoint import Endpoint


class Me(Endpoint):
    """
    Async endpoint test helper for accessing the current user's profile
    via /users/me.

    Inherits from the async base Endpoint class and provides a method to
    retrieve authenticated user details.
    """

    async def open_me(self, headers: dict[str, str] | None = None) -> None:
        """
        Send an async GET request to /users/me to retrieve the current
        user's data.

        Args:
            headers (dict[str, str] | None): Optional HTTP headers to use in
                                  the request. If not provided, default admin
                                  authorization headers will be used.

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """

        # If no custom headers provided, use admin token for authorization
        if headers is None:
            headers = await self._get_admin_authorization_headers()

        # Send GET request to the /users/me endpoint
        self.response = await self.client.get(
            url=f"{self.url_users}/me",
            headers=headers
        )

        # Parse and store the JSON response
        self.body = self.response.json()
