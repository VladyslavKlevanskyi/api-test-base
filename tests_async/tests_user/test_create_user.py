import pytest
from typing import Any

from test_data.user_test_data_messages import USER_MASSAGES
from tests_async.endpoints.user_create import CreateUser
from tests_async.endpoints.user_login import Login

from test_data.user_test_parameters import (
    INVALID_DATA_TESTS_PARAM,
    VALID_CREDENTIALS_LIST
)
from test_data.headers_test_data import (
    INVALID_HEADERS,
    HEADERS_MESSAGES
)
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
async def test_create_user(
        register_user_endpoint: CreateUser,
        user_data: dict[str, str]
) -> None:
    await register_user_endpoint.register_new_user(payload=user_data)
    # Assertions
    register_user_endpoint.check_that_status_is(201)
    register_user_endpoint.check_that_field_type_is(
        field="id", expected_type=int
    )
    register_user_endpoint.check_that_field_type_is(
        field="username", expected_type=str
    )
    register_user_endpoint.check_that_field_equals(
        field="username", expected_value=user_data["username"]
    )
    register_user_endpoint.check_that_field_type_is(
        field="is_admin", expected_type=bool
    )
    register_user_endpoint.check_that_field_equals(
        field="is_admin", expected_value=False
    )


@pytest.mark.negative
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="user_data, message, status_code",
    argvalues=[
        (data[1], data[2], data[3]) for data in INVALID_DATA_TESTS_PARAM
    ],
    ids=[title[0] for title in INVALID_DATA_TESTS_PARAM]
)
async def test_create_user_with_invalid_data(
        register_user_endpoint: CreateUser,
        user_data: dict[str, Any],
        message: str,
        status_code: int
) -> None:
    await register_user_endpoint.register_new_user(payload=user_data)
    # Assertions
    register_user_endpoint.check_that_status_is(status_code)
    register_user_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[
        (data[1], data[2]) for data in INVALID_HEADERS
    ],
    ids=[title[0] for title in INVALID_HEADERS]
)
async def test_create_user_with_invalid_headers(
        register_user_endpoint: CreateUser,
        headers: dict[str, str],
        message: str,
) -> None:
    await register_user_endpoint.register_new_user(
        payload=VALID_CREDENTIALS, headers=headers
    )
    # Assertions
    register_user_endpoint.check_that_status_is(401)
    register_user_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )


@pytest.mark.negative
@pytest.mark.asyncio
async def test_create_user_without_admin_rights(
        login_endpoint: Login,
        register_user_endpoint: CreateUser,
) -> None:
    # Login as non-admin user
    headers = await login_endpoint.login(
        payload={
            "username": TEST_USERNAME,
            "password": TEST_PASS
        }
    )
    await register_user_endpoint.register_new_user(
        payload=VALID_CREDENTIALS, headers=headers
    )
    # Assertions
    register_user_endpoint.check_that_status_is(403)
    register_user_endpoint.check_user_response_body_is_correct(
        expected_message=HEADERS_MESSAGES["no_permissions"]
    )


@pytest.mark.negative
@pytest.mark.asyncio
async def test_create_user_with_already_existing_username(
        register_user_endpoint: CreateUser
) -> None:
    await register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    await register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    # Assertions
    register_user_endpoint.check_that_status_is(400)
    register_user_endpoint.check_user_response_body_is_correct(
        expected_message=USER_MASSAGES["username_is_exist"]
    )
