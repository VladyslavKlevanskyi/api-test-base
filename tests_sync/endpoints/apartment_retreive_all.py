import requests

from tests_sync.endpoints.endpoint import Endpoint


class RetrieveAllApartments(Endpoint):
    """
    Endpoint test helper for retrieving all apartments.

    Provides a method to send a GET request to fetch all apartments
    and a method to validate the number of apartments returned.
    """

    def retrieve_all_apartments(
            self,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a GET request to retrieve all apartments.

        Args:
            headers: Optional headers for the request. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are passed
        if headers is None:
            headers = self.headers

        # Send GET request to retrieve all apartments
        self.response = requests.get(
            url=self.url_apartments,
            headers=headers
        )

        # Parse JSON body from the response
        self.body = self.response.json()

    def check_retrieved_apartments_count(self, apartments_number: int) -> None:
        """
        Assert that the number of apartments returned matches the expected
        count.

        Args:
            apartments_number: The expected number of apartments in the
                               response.
        """
        assert self.body is not None, "Response body is None"

        apartments_in_response = len(self.body)
        assert apartments_in_response == apartments_number, (
            f"Expected {apartments_number} objects, "
            f"but received {apartments_in_response}"
        )
