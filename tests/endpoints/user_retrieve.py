import requests

from tests.endpoints.endpoint import Endpoint


class RetrieveUser(Endpoint):
    """
    Endpoint test helper for retrieving a user by ID via GET /users/{user_id}.

    Inherits functionality from the base Endpoint class and provides
    a method for making authenticated requests to retrieve specific user data.
    """

    def retrieve_user_by_id(
            self,
            user_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a GET request to retrieve a user by their ID.

        Args:
            user_id (int): ID of the user to retrieve.
            headers (dict[str, str] | None): Optional HTTP headers for the
                request. If not provided, an admin bearer token will be used
                automatically.

        Side Effects:
            - Stores the HTTP response in `self.response`.
            - Stores the parsed JSON response body in `self.body`.
        """
        # Use admin token if no headers are explicitly provided
        if headers is None:
            headers = self._get_admin_authorization_headers()

        # Send GET request to the user detail endpoint
        self.response = requests.get(
            url=f"{self.url_users}/{user_id}",
            headers=headers
        )

        # Parse and store the JSON response body
        self.body = self.response.json()
