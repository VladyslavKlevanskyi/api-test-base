from tests_async.endpoints.endpoint import Endpoint


class RetrieveAllApartments(Endpoint):
    """
    Async endpoint test helper for retrieving all apartments.

    Provides an async method to fetch all apartments and
    a sync method to validate the number of returned results.
    """

    async def retrieve_all_apartments(
            self,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous GET request to retrieve all apartments.

        Args:
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send asynchronous GET request to retrieve all apartments
        self.response = await self.client.get(
            url=f"{self.url_apartments}",
            headers=headers
        )

        # Parse JSON body from the response
        self.body = self.response.json()

    def check_retrieved_apartments_count(self, apartments_number: int) -> None:
        """
        Assert that the number of apartments returned matches the expected
        count.

        Args:
            apartments_number: The expected number of apartment objects in
            the response.
        """
        assert self.body is not None, "Response body is None"
        apartments_in_response = len(self.body)
        assert apartments_in_response == apartments_number, (
            f"Expected {apartments_number} objects, but"
            f" received {apartments_in_response}"
        )
