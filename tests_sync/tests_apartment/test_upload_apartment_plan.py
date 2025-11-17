import pytest
from typing import Any

from test_data.apartment_test_data_tools import (
    generate_content,
    prepare_file_upload
)
from tests_sync.endpoints.apartment_create import CreateApartment
from tests_sync.endpoints.apartment_upload_plan import UploadApartmentPlan
from test_data.apartment_test_data import APARTMENT_DATA
from test_data.apartment_upload_test_data import (
    UPLOAD_PLAN_FIELD_VALID_PARAMS,
    UPLOAD_PLAN_FIELD_INVALID_PARAMS
)
from test_data.headers_test_data import INVALID_HEADERS


@pytest.mark.positive
@pytest.mark.parametrize(
    argnames="apartment_data, file_format, extension",
    argvalues=[
        (data[1], data[2], data[3]) for data in UPLOAD_PLAN_FIELD_VALID_PARAMS
    ],
    ids=[title[0] for title in UPLOAD_PLAN_FIELD_VALID_PARAMS]
)
def test_upload_plan(
        create_apartment_endpoint: CreateApartment,
        upload_plan_endpoint: UploadApartmentPlan,
        apartment_data: dict[str, Any],
        file_format: str,
        extension: str
) -> None:

    create_apartment_endpoint.create_apartment(payload=apartment_data)
    unit_id = create_apartment_endpoint.unit_id

    # Generate fake image bytes for upload
    file_bytes = generate_content(file_format=file_format)

    # Prepare the multipart upload file dictionary
    prepared_file = prepare_file_upload(
        content=file_bytes,
        extension=extension
    )

    upload_plan_endpoint.upload_plan_image(
        file=prepared_file,
        unit_id=unit_id
    )

    # Assert
    upload_plan_endpoint.check_that_status_is(200)
    upload_plan_endpoint.check_plan_image_field_content(extension=extension)

    upload_plan_endpoint.check_file_availability_by_link(
        expected_content=file_bytes,
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="apartment_data, file_format, extension, message",
    argvalues=[
        (
            data[1], data[2], data[3], data[4]
        ) for data in UPLOAD_PLAN_FIELD_INVALID_PARAMS
    ],
    ids=[title[0] for title in UPLOAD_PLAN_FIELD_INVALID_PARAMS]
)
def test_upload_plan_with_invalid_file_format(
        create_apartment_endpoint: CreateApartment,
        upload_plan_endpoint: UploadApartmentPlan,
        apartment_data: dict[str, Any],
        file_format: str,
        extension: str,
        message: str
) -> None:

    create_apartment_endpoint.create_apartment(payload=apartment_data)
    unit_id = create_apartment_endpoint.unit_id

    # Generate fake content in invalid format
    content_bytes = generate_content(file_format=file_format)

    # Prepare the multipart upload file dictionary
    prepared_file = prepare_file_upload(
        content=content_bytes,
        extension=extension
    )

    upload_plan_endpoint.upload_plan_image(
        file=prepared_file,
        unit_id=unit_id
    )

    # Assert
    upload_plan_endpoint.check_that_status_is(400)
    upload_plan_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_retrieve_apartment_by_id_with_invalid_headers(
        create_apartment_endpoint: CreateApartment,
        upload_plan_endpoint: UploadApartmentPlan,
        headers: dict[str, str],
        message: str,
) -> None:
    create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    unit_id = create_apartment_endpoint.unit_id

    # Generate fake JPEG image bytes
    image_bytes = generate_content(file_format="JPEG")

    # Prepare the multipart upload file dictionary
    prepared_file = prepare_file_upload(content=image_bytes, extension="jpg")

    upload_plan_endpoint.upload_plan_image(
        file=prepared_file,
        unit_id=unit_id,
        headers=headers
    )

    # Assertions
    upload_plan_endpoint.check_that_status_is(401)
    upload_plan_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
def test_retrieve_apartment_by_incorrect_unit_id(
        upload_plan_endpoint: UploadApartmentPlan,
) -> None:
    unit_id = 985463894  # Non existent apartment unit_id

    # Generate fake JPEG image bytes
    image_bytes = generate_content(file_format="JPEG")

    # Prepare the multipart upload file dictionary
    prepared_file = prepare_file_upload(content=image_bytes, extension="jpg")

    upload_plan_endpoint.upload_plan_image(
        file=prepared_file,
        unit_id=unit_id,
    )
    # Assertions
    upload_plan_endpoint.check_that_status_is(404)
    upload_plan_endpoint.check_apartment_not_found_message(
        searching_field="unit ID",
        value=unit_id
    )
