import pytest

from typing import Any

from tests_sync.endpoints.apartment_create import CreateApartment
from tests_sync.endpoints.apartment_retreive import RetrieveApartment
from test_data.apartment_test_data import APARTMENTS_DATA, APARTMENT_DATA
from test_data.headers_test_data import INVALID_HEADERS


@pytest.mark.positive
@pytest.mark.parametrize("apartment_data", APARTMENTS_DATA)
def test_retrieve_apartment_by_id(
        create_apartment_endpoint: CreateApartment,
        retrieve_apartment_endpoint: RetrieveApartment,
        apartment_data: dict[str, Any]
) -> None:
    create_apartment_endpoint.create_apartment(payload=apartment_data)
    apartment_id = create_apartment_endpoint.apartment_id
    retrieve_apartment_endpoint.retrieve_apartment_by_id(apartment_id)
    # Assertions
    retrieve_apartment_endpoint.check_that_status_is(200)
    retrieve_apartment_endpoint.check_that_field_equals(
        field="id",
        expected_value=apartment_id
    )
    retrieve_apartment_endpoint.check_that_field_type_is(
        field="updated_at",
        expected_type=str)
    retrieve_apartment_endpoint.check_that_field_equals(
        field="unit_id",
        expected_value=apartment_data["unit_id"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="unit_type",
        expected_value=apartment_data["unit_type"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="bedrooms",
        expected_value=apartment_data["bedrooms"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="bathrooms",
        expected_value=apartment_data["bathrooms"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="floor",
        expected_value=apartment_data["floor"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="area",
        expected_value=apartment_data["area"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="price",
        expected_value=apartment_data["price"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="description",
        expected_value=apartment_data["description"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="available",
        expected_value=apartment_data["available"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="plan_image",
        expected_value=apartment_data["plan_image"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="angle_ids",
        expected_value=apartment_data["angle_ids"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="images",
        expected_value=apartment_data["images"]
    )
    retrieve_apartment_endpoint.check_that_field_equals(
        field="tour",
        expected_value=apartment_data["tour"]
    )
    retrieve_apartment_endpoint.check_that_field_type_is(
        field="created_at",
        expected_type=str
    )
    retrieve_apartment_endpoint.check_that_field_type_is(
        field="updated_at",
        expected_type=str
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_retrieve_apartment_by_id_with_invalid_headers(
        create_apartment_endpoint: CreateApartment,
        retrieve_apartment_endpoint: RetrieveApartment,
        headers: dict[str, str],
        message: str,
) -> None:
    create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    apartment_id = create_apartment_endpoint.apartment_id

    retrieve_apartment_endpoint.retrieve_apartment_by_id(
        apartment_id=apartment_id,
        headers=headers
    )

    # Assertions
    retrieve_apartment_endpoint.check_that_status_is(401)
    retrieve_apartment_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
def test_retrieve_apartment_by_incorrect_id(
        retrieve_apartment_endpoint: RetrieveApartment
) -> None:
    apartment_id = 985463894  # Non existent apartment ID
    retrieve_apartment_endpoint.retrieve_apartment_by_id(
        apartment_id=apartment_id
    )
    # Assertions
    retrieve_apartment_endpoint.check_that_status_is(404)
    retrieve_apartment_endpoint.check_apartment_not_found_message(apartment_id)
