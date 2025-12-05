import requests
from typing import Any

from tests.endpoints.endpoint import Endpoint


class CreateApartment(Endpoint):
    """
    Endpoint test helper for apartment creation.

    Provides a method to send a POST request to create an apartment
    and stores the response and parsed body.
    """

    def create_apartment(
            self,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a POST request to create a new apartment.

        Args:
            payload: Dictionary containing apartment data.
            headers: Optional headers for the request. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are passed
        if headers is None:
            headers = self.headers

        # Send POST request to create a new apartment
        self.response = requests.post(
            url=self.url_apartments,
            json=payload,
            headers=headers
        )

        # Parse JSON body from the response
        self.body = self.response.json()

        # Save the apartment ID if creation succeeded
        if self.response.status_code == 201:
            self.apartment_id = self.body["id"]
            self.unit_id = self.body["unit_id"]
