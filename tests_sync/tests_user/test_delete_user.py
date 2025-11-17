import pytest

from tests_sync.endpoints.user_retrieve import RetrieveUser
from tests_sync.endpoints.user_create import CreateUser
from tests_sync.endpoints.user_delete import DeleteUser
from tests_sync.endpoints.user_login import Login
from test_data.headers_test_data import INVALID_HEADERS, HEADERS_MESSAGES
from test_data.user_test_data import (
    VALID_CREDENTIALS,
    TEST_USERNAME,
    TEST_PASS
)


@pytest.mark.positive
def test_delete_user(
        register_user_endpoint: CreateUser,
        delete_user_endpoint: DeleteUser,
        retrieve_user_endpoint: RetrieveUser,
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id
    delete_user_endpoint.delete_user_by_id(user_id=user_id)
    # Assertions
    delete_user_endpoint.check_that_status_is(200)
    delete_user_endpoint.check_delete_response_message_is_correct(user_id)
    # Check if user was deleted from DB
    retrieve_user_endpoint.retrieve_user_by_id(user_id=user_id)
    # Assertions
    retrieve_user_endpoint.check_that_status_is(
        error_message="Retrieve user with deleted ID. Returned status code:",
        code=404
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[(data[1], data[2]) for data in INVALID_HEADERS],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_delete_user_with_invalid_headers(
        register_user_endpoint: CreateUser,
        delete_user_endpoint: DeleteUser,
        headers: dict[str, str],
        message: str,
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id

    delete_user_endpoint.delete_user_by_id(user_id=user_id, headers=headers)
    # Assertions
    delete_user_endpoint.check_that_status_is(401)
    delete_user_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
def test_delete_user_without_admin_rights(
        login_endpoint: Login,
        register_user_endpoint: CreateUser,
        delete_user_endpoint: DeleteUser
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id
    # Login as non-admin user
    login_endpoint.login(
        payload={
            "username": TEST_USERNAME,
            "password": TEST_PASS
        }
    )
    delete_user_endpoint.delete_user_by_id(
        user_id=user_id,
        headers=login_endpoint.headers
    )

    # Assertions
    delete_user_endpoint.check_that_status_is(403)
    delete_user_endpoint.check_user_response_body_is_correct(
        expected_message=HEADERS_MESSAGES["no_permissions"]
    )
