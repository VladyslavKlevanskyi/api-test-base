import pytest
from typing import Any
from datetime import datetime, timezone

from test_data.apartment_test_data_messages import MESSAGES
from tests_async.endpoints.apartment_create import CreateApartment
from test_data.headers_test_data import INVALID_HEADERS
from test_data.apartment_test_data import (
    APARTMENTS_DATA,
    APARTMENT_DATA,
    APARTMENT_DATA2,
    FIELD_VALIDATION_VALID_TEST_PARAMS,
    FIELD_VALIDATION_INVALID_TEST_PARAMS
)


@pytest.mark.positive
@pytest.mark.asyncio
@pytest.mark.parametrize("apartment_data", APARTMENTS_DATA)
async def test_create_apartment(
        create_apartment_endpoint: CreateApartment,
        apartment_data: dict[str, Any]
) -> None:
    await create_apartment_endpoint.create_apartment(payload=apartment_data)
    # Assertions
    create_apartment_endpoint.check_that_status_is(201)
    create_apartment_endpoint.check_that_field_type_is(
        field="id",
        expected_type=int)
    create_apartment_endpoint.check_that_field_type_is(
        field="created_at",
        expected_type=str)
    create_apartment_endpoint.check_that_field_type_is(
        field="updated_at",
        expected_type=str)
    create_apartment_endpoint.check_that_field_equals(
        field="unit_id",
        expected_value=apartment_data["unit_id"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="unit_type",
        expected_value=apartment_data["unit_type"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="bedrooms",
        expected_value=apartment_data["bedrooms"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="bathrooms",
        expected_value=apartment_data["bathrooms"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="floor",
        expected_value=apartment_data["floor"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="area",
        expected_value=apartment_data["area"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="price",
        expected_value=apartment_data["price"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="description",
        expected_value=apartment_data["description"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="available",
        expected_value=apartment_data["available"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="plan_image",
        expected_value=apartment_data["plan_image"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="angle_ids",
        expected_value=apartment_data["angle_ids"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="images",
        expected_value=apartment_data["images"]
    )
    create_apartment_endpoint.check_that_field_equals(
        field="tour",
        expected_value=apartment_data["tour"]
    )


@pytest.mark.positive
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="field, apartment_data, expected_value",
    argvalues=[
        (
            data[1], data[2], data[3]
        ) for data in FIELD_VALIDATION_VALID_TEST_PARAMS
    ],
    ids=[title[0] for title in FIELD_VALIDATION_VALID_TEST_PARAMS]
)
async def test_create_apartment_field_validation_with_valid_data(
        create_apartment_endpoint: CreateApartment,
        field: str,
        apartment_data: dict[str, Any],
        expected_value: str,
) -> None:
    await create_apartment_endpoint.create_apartment(payload=apartment_data)
    # Assertions
    create_apartment_endpoint.check_that_status_is(201)
    create_apartment_endpoint.check_that_field_equals(
        field=field,
        expected_value=expected_value
    )


@pytest.mark.asyncio
@pytest.mark.positive
async def test_create_apartment_created_and_updated_at_fields(
        create_apartment_endpoint: CreateApartment,
) -> None:
    time_tolerance = 5  # acceptable time difference
    await create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    time_now = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(
        timespec="seconds"
    )
    # Assertions
    create_apartment_endpoint.check_that_status_is(201)
    create_apartment_endpoint.check_create_and_update_fields(
        time_tolerance=time_tolerance,
        field="created_at",
        expected_value=time_now
    )
    create_apartment_endpoint.check_create_and_update_fields(
        time_tolerance=time_tolerance,
        field="updated_at",
        expected_value=time_now
    )


@pytest.mark.negative
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="apartment_data, expected_error",
    argvalues=[
        (data[1], data[2]) for data in FIELD_VALIDATION_INVALID_TEST_PARAMS
    ],
    ids=[title[0] for title in FIELD_VALIDATION_INVALID_TEST_PARAMS]
)
async def test_create_apartment_field_validation_with_invalid_data(
        create_apartment_endpoint: CreateApartment,
        apartment_data: dict[str, Any],
        expected_error: tuple[str, str]
) -> None:
    await create_apartment_endpoint.create_apartment(payload=apartment_data)
    # Assertions
    create_apartment_endpoint.check_that_status_is(422)
    create_apartment_endpoint.check_field_validation_error_response(
        expected_error
    )


@pytest.mark.negative
@pytest.mark.asyncio
async def test_create_apartment_with_duplicate_unit_id_fails(
        create_apartment_endpoint: CreateApartment,
) -> None:
    await create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    new_data = APARTMENT_DATA2
    new_data["unit_id"] = APARTMENT_DATA["unit_id"]
    await create_apartment_endpoint.create_apartment(payload=new_data)
    # Assertions
    create_apartment_endpoint.check_that_status_is(400)
    create_apartment_endpoint.check_user_response_body_is_correct(
        expected_message=MESSAGES["apartment_is_exist"]
    )


@pytest.mark.negative
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
async def test_create_apartment_with_invalid_headers(
        create_apartment_endpoint: CreateApartment,
        headers: dict[str, str],
        message: str,
) -> None:
    await create_apartment_endpoint.create_apartment(
        payload=APARTMENT_DATA,
        headers=headers
    )
    # Assertions
    create_apartment_endpoint.check_that_status_is(401)
    create_apartment_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )
