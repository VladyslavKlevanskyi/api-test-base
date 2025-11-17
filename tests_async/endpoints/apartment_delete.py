from tests_async.endpoints.endpoint import Endpoint


class DeleteApartment(Endpoint):
    """
    Async endpoint test helper for deleting an apartment.

    Provides an async method to send a DELETE request and
    a sync method to validate the response message.
    """

    async def delete_apartment_by_id(
            self,
            apartment_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous DELETE request to remove an apartment by ID.

        Args:
            apartment_id: ID of the apartment to be deleted.
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send asynchronous DELETE request to /apartments/{id}
        self.response = await self.client.delete(
            url=f"{self.url_apartments}/{apartment_id}",
            headers=headers
        )

        # Parse JSON response body
        self.body = self.response.json()

    def check_delete_response_message_is_correct(
            self, apartment_id: int
    ) -> None:
        """
        Assert that the success message in the delete response is correct.

        Args:
            apartment_id: ID of the apartment that was deleted.
        """
        assert self.body is not None, "Response body is None"
        expected_message = (
            f"Apartment with ID {apartment_id} has been deleted."
        )
        actual_message = self.body["message"]
        assert expected_message == actual_message, (
            f"Expected message: {expected_message},"
            f" Actual message: {actual_message}"
        )
