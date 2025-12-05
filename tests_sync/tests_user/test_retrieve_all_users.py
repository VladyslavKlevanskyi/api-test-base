import pytest

from tests_sync.endpoints.user_login import Login
from tests_sync.endpoints.user_retrieve_all import RetrieveAllUsers
from test_data.headers_test_data import INVALID_HEADERS, HEADERS_MESSAGES
from test_data.user_test_data import (
    TEST_USERNAME,
    TEST_PASS
)


@pytest.mark.smoke
@pytest.mark.positive
def test_retrieve_all_users(
        create_few_users: list,
        retrieve_users_endpoint: RetrieveAllUsers
) -> None:
    number_of_created_users = len(create_few_users)
    retrieve_users_endpoint.retrieve_all_users()
    # Assertions
    retrieve_users_endpoint.check_that_status_is(200)
    retrieve_users_endpoint.check_retrieved_users_not_less_than_created(
        created_users=number_of_created_users
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[
        (data[1], data[2]) for data in INVALID_HEADERS
    ],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_retrieve_all_users_with_invalid_headers(
        create_few_users: list,
        retrieve_users_endpoint: RetrieveAllUsers,
        headers: dict[str, str],
        message: str,
) -> None:
    retrieve_users_endpoint.retrieve_all_users(headers=headers)

    # Assertions
    retrieve_users_endpoint.check_that_status_is(401)
    retrieve_users_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
def test_retrieve_all_users_without_admin_rights(
        create_few_users: list,
        retrieve_users_endpoint: RetrieveAllUsers,
        login_endpoint: Login
) -> None:
    # Login as non-admin user
    login_endpoint.login(
        payload={
            "username": TEST_USERNAME,
            "password": TEST_PASS
        }
    )
    retrieve_users_endpoint.retrieve_all_users(headers=login_endpoint.headers)

    # Assertions
    retrieve_users_endpoint.check_that_status_is(403)
    retrieve_users_endpoint.check_user_response_body_is_correct(
        expected_message=HEADERS_MESSAGES["no_permissions"]
    )
