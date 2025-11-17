import pytest

from tests_async.endpoints.user_create import CreateUser
from tests_async.endpoints.user_login import Login
from tests_async.endpoints.user_retrieve import RetrieveUser
from test_data.headers_test_data import INVALID_HEADERS, HEADERS_MESSAGES
from test_data.user_test_parameters import VALID_CREDENTIALS_LIST
from test_data.user_test_data import (
    VALID_CREDENTIALS,
    TEST_USERNAME,
    TEST_PASS
)


@pytest.mark.positive
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="user_data",
    argvalues=[data[1] for data in VALID_CREDENTIALS_LIST],
    ids=[title[0] for title in VALID_CREDENTIALS_LIST]
)
async def test_retrieve_user_by_id(
        register_user_endpoint: CreateUser,
        retrieve_user_endpoint: RetrieveUser,
        user_data: dict[str, str]
) -> None:
    await register_user_endpoint.register_new_user(payload=user_data)
    user_id = register_user_endpoint.user_id
    await retrieve_user_endpoint.retrieve_user_by_id(user_id=user_id)
    # Assertions
    retrieve_user_endpoint.check_that_status_is(200)
    retrieve_user_endpoint.check_that_field_type_is(
        field="id", expected_type=int
    )
    retrieve_user_endpoint.check_that_field_equals(
        field="id", expected_value=user_id
    )
    retrieve_user_endpoint.check_that_field_type_is(
        field="username", expected_type=str
    )
    retrieve_user_endpoint.check_that_field_equals(
        field="username", expected_value=user_data["username"]
    )
    retrieve_user_endpoint.check_that_field_type_is(
        field="is_admin", expected_type=bool
    )
    retrieve_user_endpoint.check_that_field_equals(
        field="is_admin", expected_value=False
    )


@pytest.mark.negative
@pytest.mark.asyncio
async def test_retrieve_user_by_incorrect_id(
        retrieve_user_endpoint: RetrieveUser
) -> None:
    user_id = 985463894  # Non existent user ID
    await retrieve_user_endpoint.retrieve_user_by_id(
        user_id=user_id
    )
    # Assertions
    retrieve_user_endpoint.check_that_status_is(404)
    retrieve_user_endpoint.check_user_not_found_message(user_id=user_id)


@pytest.mark.negative
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[
        (data[1], data[2]) for data in INVALID_HEADERS
    ],
    ids=[title[0] for title in INVALID_HEADERS]
)
async def test_retrieve_user_by_id_with_invalid_headers(
        register_user_endpoint: CreateUser,
        retrieve_user_endpoint: RetrieveUser,
        headers: dict[str, str],
        message: str,
) -> None:
    await register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id
    await retrieve_user_endpoint.retrieve_user_by_id(
        user_id=user_id,
        headers=headers
    )
    # Assertions
    retrieve_user_endpoint.check_that_status_is(401)
    retrieve_user_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
@pytest.mark.asyncio
async def test_retrieve_user_by_id_without_admin_rights(
        login_endpoint: Login,
        register_user_endpoint: CreateUser,
        retrieve_user_endpoint: RetrieveUser
) -> None:
    await register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id
    # Login as non-admin user
    headers = await login_endpoint.login(
        payload={
            "username": TEST_USERNAME,
            "password": TEST_PASS
        }
    )
    await retrieve_user_endpoint.retrieve_user_by_id(
        user_id=user_id,
        headers=headers
    )
    # Assertions
    retrieve_user_endpoint.check_that_status_is(403)
    retrieve_user_endpoint.check_user_response_body_is_correct(
        expected_message=HEADERS_MESSAGES["no_permissions"]
    )
