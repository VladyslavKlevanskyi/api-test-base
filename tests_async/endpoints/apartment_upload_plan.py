from typing import Any

from tests_async.endpoints.endpoint import Endpoint


class UploadApartmentPlan(Endpoint):
    """
    Async endpoint test helper for uploading apartment plan images.

    Provides methods to upload a floor plan image for a specific apartment,
    validate that the uploaded file is saved and accessible, and clean up
    test files after execution.
    """

    async def upload_plan_image(
        self,
        unit_id: int,
        file: dict[str, Any],
        headers: dict[str, str] | None = None
    ) -> None:
        """
        Send an asynchronous PATCH request to upload a floor plan image
        for the specified apartment.

        Args:
            unit_id: The unit ID of the apartment that the image will be
                     linked to.
            file: A dictionary containing file metadata and content
                  (see httpx format).
            headers: Optional request headers. If not provided,
                     authorization headers will be generated using a valid
                     token.
        """
        # generate authorization headers
        if headers is None:
            headers = await self._get_authorization_headers()

        # Send the PATCH request with multipart file
        self.response = await self.client.patch(
            url=f"{self.url_apartments}/upload-plan/{unit_id}",
            files=file,
            headers=headers
        )

        # Parse and store JSON response body
        self.body = self.response.json()

    @staticmethod
    def _generate_plan_image_file_name(
            body: dict[str, Any],
            extension: str
    ) -> str:
        """
        Generate a filename for the uploaded image based on apartment
        attributes.

        Args:
            body: JSON response body containing apartment details.
            extension: File extension (e.g., "jpg", "png").

        Returns:
            str: The generated filename.
        """
        filename = (
            f"unit_id-{body['unit_id']:04d}_bedrooms-{body['bedrooms']}_"
            f"floor-{body['floor']}.{extension}"
        )
        return filename

    def check_plan_image_field_content(self, extension: str) -> None:
        """
        Assert that the `plan_image` field in the response contains the
        correct file path.

        Args:
            extension: File extension (e.g., "jpg", "png").
        """

        filename = self._generate_plan_image_file_name(self.body, extension)

        assert self.body["plan_image"] == f"/apartment/plans/{filename}"

    async def check_file_availability_by_link(
            self,
            expected_content: bytes
    ) -> None:
        """
        Send a GET request to the plan image URL and verify its content.

        Args:
            expected_content: The expected binary content of the uploaded file.
        """

        response = await self.client.get(
            url=self.body["plan_image"],
        )

        assert response.content == expected_content, (
            "The file content does not match what was expected"
        )
