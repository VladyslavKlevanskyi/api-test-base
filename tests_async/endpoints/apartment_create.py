from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class CreateApartment(Endpoint):
    """
    Async endpoint test helper for apartment creation.

    Provides an async method to send a POST request to create an apartment
    and stores the response and parsed body.
    """

    async def create_apartment(
            self,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous POST request to create a new apartment.

        Args:
            payload: Dictionary containing apartment data.
            headers: Optional headers for the request. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send POST request to create a new apartment
        self.response = await self.client.post(
            url=self.url_apartments,
            json=payload,
            headers=headers
        )

        # Parse response JSON body
        self.body = self.response.json()

        # Save ID and unit_id if creation was successful
        if self.response.status_code == 201:
            self.apartment_id = self.body["id"]
            self.unit_id = self.body["unit_id"]
