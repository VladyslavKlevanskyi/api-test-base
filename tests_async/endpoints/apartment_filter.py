from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class FilterApartments(Endpoint):
    """
    Async endpoint test helper for filtering apartments.

    Provides an async method to send a POST request with filters
    and a sync method to validate the number of returned results.
    """

    async def retrieve_apartments_by_field_value(
            self,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous POST request to filter apartments based on field
        values.

        Args:
            payload: Dictionary of filter parameters.
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send asynchronous POST request to /apartments/filter
        self.response = await self.client.post(
            url=f"{self.url_apartments}/filter",
            json=payload,
            headers=headers
        )

        # Parse JSON response body
        self.body = self.response.json()

    def check_apartment_count(self, count: int) -> None:
        """
        Assert that the number of returned apartments matches the expected
        count.

        Args:
            count: Expected number of apartment objects in the response.
        """
        assert self.body is not None, "Response body is None"

        apartments_in_response = len(self.body)
        assert apartments_in_response == count, (
            f"Expected {count} objects, but"
            f" received {apartments_in_response}"
        )
