import allure
import pytest

from tests.endpoints.apartment_create import CreateApartment
from tests.endpoints.apartment_retreive_all import (
    RetrieveAllApartments
)
from test_data.apartment_test_data import APARTMENTS_NUMBER
from test_data.headers_test_data import INVALID_HEADERS


@allure.story("Positive")
@pytest.mark.smoke
@pytest.mark.positive
def test_get_all_apartments(
        create_few_apartments: int,
        retrieve_apartments_endpoint: RetrieveAllApartments
) -> None:
    retrieve_apartments_endpoint.retrieve_all_apartments()
    # Assertions
    retrieve_apartments_endpoint.check_that_status_is(200)
    retrieve_apartments_endpoint.check_retrieved_apartments_count(
        apartments_number=APARTMENTS_NUMBER
    )


@allure.story("Negative")
@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_get_all_apartments_with_invalid_headers(
        create_few_apartments: CreateApartment,
        retrieve_apartments_endpoint: RetrieveAllApartments,
        headers: dict[str, str],
        message: str
) -> None:
    retrieve_apartments_endpoint.retrieve_all_apartments(
        headers=headers
    )

    # Assertions
    retrieve_apartments_endpoint.check_that_status_is(401)
    retrieve_apartments_endpoint.check_error_response_body_is_correct(
        expected_message=message
    )
