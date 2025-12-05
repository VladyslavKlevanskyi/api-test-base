import requests

from tests.endpoints.endpoint import Endpoint


class DeleteApartment(Endpoint):
    """
    Endpoint test helper for deleting an apartment.

    Provides methods to send DELETE requests and check
    correctness of the deletion response.
    """

    def delete_apartment_by_id(
            self,
            apartment_id: int,
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send a DELETE request to remove an apartment by ID.

        Args:
            apartment_id: ID of the apartment to be deleted.
            headers: Optional request headers. If not provided,
                     default authorization headers will be used.
        """
        # Use default authorization headers if none are provided
        if headers is None:
            headers = self.headers

        # Send DELETE request to /apartments/{id}
        self.response = requests.delete(
            url=f"{self.url_apartments}/{apartment_id}",
            headers=headers
        )

        # Parse JSON response body
        self.body = self.response.json()

    def check_delete_response_message_is_correct(
            self,
            apartment_id: int
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
