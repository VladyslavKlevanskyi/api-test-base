import pytest
from typing import Any

from test_data.apartment_test_data import (
    ONE_FIELD_FILTRATION_PARAMS,
    FEW_FIELD_FILTRATION_PARAMS
)
from tests.endpoints.apartment_filter import FilterApartments
from test_data.headers_test_data import INVALID_HEADERS


@pytest.mark.positive
@pytest.mark.parametrize(
    argnames="field, value, expected_count",
    argvalues=[
        (data[1], data[2], data[3]) for data in ONE_FIELD_FILTRATION_PARAMS
    ],
    ids=[title[0] for title in ONE_FIELD_FILTRATION_PARAMS]
)
def test_filter_apartments_by_one_field(
        create_few_specific_apartments: list,
        filter_apartment_endpoint: FilterApartments,
        field: str,
        value: int | float | bool | str,
        expected_count: int,
) -> None:
    filter_apartment_endpoint.retrieve_apartments_by_field_value(
        payload={field: value}
    )
    # Assertions
    filter_apartment_endpoint.check_that_status_is(200)
    filter_apartment_endpoint.check_apartment_count(count=expected_count)


@pytest.mark.positive
@pytest.mark.parametrize(
    argnames="payload, expected_count",
    argvalues=[
        (data[1], data[2]) for data in FEW_FIELD_FILTRATION_PARAMS
    ],
    ids=[title[0] for title in FEW_FIELD_FILTRATION_PARAMS]
)
def test_filter_apartments_by_few_fields(
        create_few_specific_apartments: list,
        filter_apartment_endpoint: FilterApartments,
        payload: dict[str, Any],
        expected_count: int,
) -> None:
    filter_apartment_endpoint.retrieve_apartments_by_field_value(
        payload=payload
    )
    # Assertions
    filter_apartment_endpoint.check_that_status_is(200)
    filter_apartment_endpoint.check_apartment_count(count=expected_count)


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_filter_apartments_with_invalid_headers(
        create_few_specific_apartments: list,
        filter_apartment_endpoint: FilterApartments,
        headers: dict[str, str],
        message: str,
) -> None:

    filter_apartment_endpoint.retrieve_apartments_by_field_value(
        payload={"min_bedrooms": 5, "max_bedrooms": 8},
        headers=headers
    )

    # Assertions
    filter_apartment_endpoint.check_that_status_is(401)
    filter_apartment_endpoint.check_error_response_body_is_correct(
        expected_message=message
    )
