import allure
import requests

from tests.endpoints.endpoint import Endpoint


class RetrieveApartment(Endpoint):
    """
    Endpoint test helper for retrieving apartment data.

    Provides methods to retrieve an apartment by its primary ID
    or by the unit ID, and stores the response and parsed body.
    """

    def retrieve_apartment_by_id(
            self,
            apartment_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a GET request to retrieve an apartment by its ID.

        Args:
            apartment_id: The primary ID of the apartment.
            headers: Optional headers for the request. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are passed
        if headers is None:
            headers = self.headers

        with allure.step("Send GET request to retrieve the apartment by ID"):
            self.response = requests.get(
                url=f"{self.url_apartments}/{apartment_id}",
                headers=headers
            )

            # Parse JSON body from the response
            self.body = self.response.json()

    def retrieve_apartment_by_unit_id(
            self,
            unit_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a GET request to retrieve an apartment by its unit ID.

        Args:
            unit_id: The unit ID associated with the apartment.
            headers: Optional headers for the request. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are passed
        if headers is None:
            headers = self.headers

        with allure.step(
                "Send GET request to retrieve the apartment by unit_id"
        ):
            self.response = requests.get(
                url=f"{self.url_apartments}/unit/{unit_id}",
                headers=headers
            )

            # Parse JSON body from the response
            self.body = self.response.json()
