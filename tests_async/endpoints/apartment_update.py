from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class UpdateApartment(Endpoint):
    """
    Async endpoint test helper for updating apartment data.

    Provides an async method to send a PATCH request to update apartment
    fields, and a sync method to verify that all fields except one remain
    unchanged.
    """

    async def update_apartment(
            self,
            apartment_id: int,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> dict[str, Any]:
        """
        Send an asynchronous PATCH request to update an apartment by its ID.

        Args:
            apartment_id: ID of the apartment to update.
            payload: Dictionary containing fields to update.
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.

        Returns:
            The JSON response body as a dictionary.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send PATCH request to update a new apartment
        self.response = await self.client.patch(
            url=f"{self.url_apartments}/{apartment_id}",
            json=payload,
            headers=headers
        )

        # Parse response JSON body
        self.body = self.response.json()

        return self.body

    def check_all_fields_except_one_remain_unchanged(
            self,
            updated_field: str,
            rest_fields: dict[str, Any]
    ) -> None:
        """
        Assert that all fields except the updated one remain unchanged
        in the response body.

        Args:
            updated_field: The field that was intentionally updated.
            rest_fields: Dictionary of all other fields with their expected
                        values.
        """
        # Remove the updated field from the comparison
        rest_fields.pop(updated_field)

        # Validate that all other fields have expected values
        for field, value in rest_fields.items():
            assert self.body[field] == value, (
                f"Expected field value: {value}. "
                f"Actual field value: {self.body[field]}"
            )
