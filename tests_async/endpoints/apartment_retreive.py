from tests_async.endpoints.endpoint import Endpoint


class RetrieveApartment(Endpoint):
    """
    Async endpoint test helper for retrieving apartment data.

    Provides async methods to retrieve an apartment by its primary ID
    or by the unit ID, and stores the response and parsed body.
    """

    async def retrieve_apartment_by_id(
            self,
            apartment_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous GET request to retrieve an apartment by its ID.

        Args:
            apartment_id: The primary ID of the apartment.
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send asynchronous GET request to retrieve the apartment by ID
        self.response = await self.client.get(
            url=f"{self.url_apartments}/{apartment_id}",
            headers=headers
        )

        # Parse JSON body from the response
        self.body = self.response.json()

    async def retrieve_apartment_by_unit_id(
            self,
            unit_id: int,
            headers: dict | None = None
    ) -> None:
        """
        Send an asynchronous GET request to retrieve an apartment by its
        unit ID.

        Args:
            unit_id: The unit ID associated with the apartment.
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send asynchronous GET request to retrieve the apartment by unit_id
        self.response = await self.client.get(
            url=f"{self.url_apartments}/unit/{unit_id}",
            headers=headers
        )

        # Parse JSON body from the response
        self.body = self.response.json()
