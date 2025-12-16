import allure
import pytest

from tests.endpoints.apartment_retreive import RetrieveApartment
from tests.endpoints.apartment_create import CreateApartment
from tests.endpoints.apartment_delete import DeleteApartment
from test_data.apartment_test_data import APARTMENT_DATA
from test_data.headers_test_data import INVALID_HEADERS


@allure.story("Positive")
@pytest.mark.smoke
@pytest.mark.positive
def test_delete_apartment(
        create_apartment_endpoint: CreateApartment,
        delete_apartment_endpoint: DeleteApartment,
        retrieve_apartment_endpoint: RetrieveApartment
) -> None:
    create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    apartment_id = create_apartment_endpoint.apartment_id
    delete_apartment_endpoint.delete_apartment_by_id(apartment_id=apartment_id)
    # Assertions
    delete_apartment_endpoint.check_that_status_is(200)
    delete_apartment_endpoint.check_delete_response_message_is_correct(
        apartment_id
    )
    with allure.step("Check if apartment was deleted from DB"):
        retrieve_apartment_endpoint.retrieve_apartment_by_id(
            apartment_id=apartment_id
        )
        # Assertions
        retrieve_apartment_endpoint.check_that_status_is(
            error_message=(
                "Retrieve apartment with deleted ID. Returned status code:"
            ),
            code=404
        )


@allure.story("Negative")
@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_delete_apartment_with_invalid_headers(
        create_apartment_endpoint: CreateApartment,
        delete_apartment_endpoint: DeleteApartment,
        headers: dict[str, str],
        message: str,
) -> None:
    create_apartment_endpoint.create_apartment(payload=APARTMENT_DATA)
    apartment_id = create_apartment_endpoint.apartment_id

    delete_apartment_endpoint.delete_apartment_by_id(
        apartment_id=apartment_id,
        headers=headers
    )

    # Assertions
    delete_apartment_endpoint.check_that_status_is(401)
    delete_apartment_endpoint.check_error_response_body_is_correct(
        expected_message=message
    )


@allure.story("Negative")
@pytest.mark.negative
def test_delete_apartment_by_incorrect_id(
        delete_apartment_endpoint: DeleteApartment
) -> None:
    apartment_id = 985463894  # Non existent apartment ID
    delete_apartment_endpoint.delete_apartment_by_id(apartment_id=apartment_id)
    # Assertions
    delete_apartment_endpoint.check_that_status_is(404)
    delete_apartment_endpoint.check_apartment_not_found_message(apartment_id)
