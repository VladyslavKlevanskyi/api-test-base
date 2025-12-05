from typing import Any

import requests

from tests.endpoints.endpoint import Endpoint


class UpdateApartment(Endpoint):
    """
    Endpoint test helper for updating apartment data.

    Provides a method to send a PATCH request to update apartment fields,
    and a method to verify that all fields except one remain unchanged.
    """

    def update_apartment(
            self,
            apartment_id: int,
            payload: dict[str, Any],
            headers: dict[str, str] | None = None
    ) -> dict[str, Any]:
        """
        Send a PATCH request to update an apartment by its ID.

        Args:
            apartment_id: ID of the apartment to update.
            payload: Dictionary containing fields to update.
            headers: Optional request headers. If not provided,
                     default authorization headers will be used.

        Returns:
            The JSON response body as a dictionary.
        """
        # Use default authorization headers if none are passed
        if headers is None:
            headers = self.headers

        # Send PATCH request to update an existing apartment
        self.response = requests.patch(
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
        Assert that all fields except the updated one remain unchanged in the
        response body.

        Args:
            updated_field: The field that was updated.
            rest_fields: Dictionary of other fields with their expected values.
        """
        # Remove the updated field from rest_fields before checking
        rest_fields.pop(updated_field)

        # Check that all other fields match expected values
        for field, value in rest_fields.items():
            assert self.body[field] == value, (
                f"Expected field value: {value}. "
                f"Actual field value: {self.body[field]}"
            )
