import pytest
from time import sleep
from datetime import datetime, timezone
from typing import Any

from test_data.apartment_test_data_messages import MESSAGES
from test_data.apartment_test_data_tools import get_apartment_data
from tests_sync.endpoints.apartment_update import UpdateApartment
from tests_sync.endpoints.apartment_create import CreateApartment
from test_data.headers_test_data import INVALID_HEADERS

from test_data.apartment_test_data import (
    APARTMENTS_DATA,
    FIELD_UPDATE_VALID_TEST_PARAMS,
    FIELD_UPDATE_INVALID_TEST_PARAMS,
)


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("payload", APARTMENTS_DATA)
def test_update_apartment_body(
        create_apartment_endpoint: CreateApartment,
        update_apartment_endpoint: UpdateApartment,
        payload: dict[str, Any]
) -> None:
    # acceptable time difference in update_at and create_at fields
    time_tolerance = 2

    create_apartment_endpoint.create_apartment(
        payload=get_apartment_data()
    )
    creation_time = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(
        timespec="seconds"
    )
    apartment_id = create_apartment_endpoint.apartment_id

    # sleep for making updated time different
    sleep(5)

    update_time = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(
        timespec="seconds"
    )
    update_apartment_endpoint.update_apartment(
        apartment_id=apartment_id,
        payload=payload
    )

    # Assertions
    update_apartment_endpoint.check_that_status_is(200)
    update_apartment_endpoint.check_that_field_equals(
        field="id",
        expected_value=apartment_id)
    update_apartment_endpoint.check_that_field_equals(
        field="unit_id",
        expected_value=payload["unit_id"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="unit_type",
        expected_value=payload["unit_type"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="bedrooms",
        expected_value=payload["bedrooms"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="bathrooms",
        expected_value=payload["bathrooms"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="floor",
        expected_value=payload["floor"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="area",
        expected_value=payload["area"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="price",
        expected_value=payload["price"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="description",
        expected_value=payload["description"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="available",
        expected_value=payload["available"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="plan_image",
        expected_value=payload["plan_image"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="angle_ids",
        expected_value=payload["angle_ids"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="images",
        expected_value=payload["images"]
    )
    update_apartment_endpoint.check_that_field_equals(
        field="tour",
        expected_value=payload["tour"]
    )
    update_apartment_endpoint.check_create_and_update_fields(
        time_tolerance=time_tolerance,
        field="created_at",
        expected_value=creation_time
    )
    update_apartment_endpoint.check_create_and_update_fields(
        time_tolerance=time_tolerance,
        field="updated_at",
        expected_value=update_time
    )


@pytest.mark.positive
@pytest.mark.parametrize(
    argnames="field, value, expected_value",
    argvalues=[
        (data[1], data[2], data[3]) for data in FIELD_UPDATE_VALID_TEST_PARAMS
    ],
    ids=[title[0] for title in FIELD_UPDATE_VALID_TEST_PARAMS]
)
def test_update_one_field_in_apartment_with_valid_data(
        create_apartment_endpoint: CreateApartment,
        update_apartment_endpoint: UpdateApartment,
        field: str,
        value: int | float | bool | str | list,
        expected_value: int | float | bool | str | list,
) -> None:
    apartment_valid_data = get_apartment_data()
    create_apartment_endpoint.create_apartment(
        payload=apartment_valid_data
    )
    apartment_id = create_apartment_endpoint.apartment_id

    update_apartment_endpoint.update_apartment(
        apartment_id=apartment_id,
        payload={field: value}
    )

    # Assertions
    update_apartment_endpoint.check_that_status_is(200)
    update_apartment_endpoint.check_that_field_equals(
        field=field,
        expected_value=expected_value)
    update_apartment_endpoint.check_all_fields_except_one_remain_unchanged(
        updated_field=field,
        rest_fields=apartment_valid_data,
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="payload, expected_error",
    argvalues=[
        (data[1], data[2]) for data in FIELD_UPDATE_INVALID_TEST_PARAMS
    ],
    ids=[title[0] for title in FIELD_UPDATE_INVALID_TEST_PARAMS]
)
def test_update_one_field_in_apartment_with_invalid_data(
        create_apartment_endpoint: CreateApartment,
        update_apartment_endpoint: UpdateApartment,
        payload: dict[str, Any],
        expected_error: tuple[str, str]
) -> None:
    apartment_valid_data = get_apartment_data()
    create_apartment_endpoint.create_apartment(
        payload=apartment_valid_data
    )
    apartment_id = create_apartment_endpoint.apartment_id

    update_apartment_endpoint.update_apartment(
        apartment_id=apartment_id,
        payload=payload
    )
    # Assertions
    update_apartment_endpoint.check_that_status_is(422)
    update_apartment_endpoint.check_field_validation_error_response(
        expected_error
    )


@pytest.mark.negative
def test_update_apartment_with_duplicate_unit_id_fails(
        create_two_apartments_for_duplicate_test: tuple,
        update_apartment_endpoint: UpdateApartment,
) -> None:
    (
        first_apartment_id,
        second_apartment_id,
        first_apartment_unit_id
    ) = create_two_apartments_for_duplicate_test

    update_apartment_endpoint.update_apartment(
        apartment_id=second_apartment_id,
        payload={"unit_id": first_apartment_unit_id}
    )

    # Assertions
    update_apartment_endpoint.check_that_status_is(400)
    update_apartment_endpoint.check_user_response_body_is_correct(
        expected_message=MESSAGES["apartment_is_exist"]
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_update_apartment_with_invalid_headers(
        create_apartment_endpoint: CreateApartment,
        update_apartment_endpoint: UpdateApartment,
        headers: dict[str, str],
        message: str,
) -> None:
    apartment_valid_data1 = get_apartment_data()
    apartment_valid_data2 = get_apartment_data()

    create_apartment_endpoint.create_apartment(
        payload=apartment_valid_data1,
    )
    apartment_id = create_apartment_endpoint.apartment_id

    update_apartment_endpoint.update_apartment(
        apartment_id=apartment_id,
        payload=apartment_valid_data2,
        headers=headers
    )
    # Assertions
    update_apartment_endpoint.check_that_status_is(401)
    update_apartment_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )
