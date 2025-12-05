import pytest

from typing import Any

from tests_sync.endpoints.user_create import CreateUser
from tests_sync.endpoints.user_login import Login
from tests_sync.endpoints.user_password import UpdateUserPass
from test_data.headers_test_data import INVALID_HEADERS, HEADERS_MESSAGES
from test_data.user_test_data import (
    VALID_CREDENTIALS,
    TEST_USERNAME,
    TEST_PASS,
    NEW_VALID_PASS
)
from test_data.user_test_parameters import (
    INVALID_PASS_FIELD_TESTS_PARAM,
    BOUNDARY_VALUES_TESTS_PARAM
)


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize(
    argnames="new_password",
    argvalues=[data[1]["password"] for data in BOUNDARY_VALUES_TESTS_PARAM],
    ids=[title[0] for title in BOUNDARY_VALUES_TESTS_PARAM]
)
def test_update_user_password(
        register_user_endpoint: CreateUser,
        update_user_password_endpoint: UpdateUserPass,
        login_endpoint: Login,
        new_password: str
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id

    update_user_password_endpoint.update_user_password(
        user_id=user_id,
        payload={"password": new_password}
    )
    # Assertions
    update_user_password_endpoint.check_that_status_is(200)
    update_user_password_endpoint.check_that_field_type_is(
        field="id", expected_type=int
    )
    update_user_password_endpoint.check_that_field_equals(
        field="id", expected_value=user_id
    )
    update_user_password_endpoint.check_that_field_type_is(
        field="username", expected_type=str
    )
    update_user_password_endpoint.check_that_field_equals(
        field="username", expected_value=VALID_CREDENTIALS["username"]
    )
    update_user_password_endpoint.check_that_field_type_is(
        field="is_admin", expected_type=bool
    )
    update_user_password_endpoint.check_that_field_equals(
        field="is_admin", expected_value=False
    )
    # check that password was updated
    login_endpoint.login(
        payload={
            "username": VALID_CREDENTIALS["username"],
            "password": new_password
        }
    )
    login_endpoint.check_that_status_is(
        error_message="Login with new password failed. Returned status code:",
        code=200
    )


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="payload, message, status_code",
    argvalues=[
        (data[1], data[2], data[3]) for data in INVALID_PASS_FIELD_TESTS_PARAM
    ],
    ids=[title[0] for title in INVALID_PASS_FIELD_TESTS_PARAM]
)
def test_update_user_password_with_invalid_data(
        register_user_endpoint: CreateUser,
        update_user_password_endpoint: UpdateUserPass,
        login_endpoint: Login,
        payload: dict[str, Any],
        message: str,
        status_code: int
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id

    update_user_password_endpoint.update_user_password(
        user_id=user_id,
        payload=payload
    )
    # Assertions
    update_user_password_endpoint.check_that_status_is(status_code)
    update_user_password_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )
    # check that password was NOT updated
    login_endpoint.login(
        payload={
            "username": VALID_CREDENTIALS["username"],
            "password": payload.get("password")
        }
    )
    login_endpoint.check_that_status_is(
        error_message="Login with new password. Returned status code:",
        code=422
    )


@pytest.mark.negative
def test_update_user_password_by_by_incorrect_id(
        update_user_password_endpoint: UpdateUserPass
) -> None:
    user_id = 33455262423  # Non existent user ID
    update_user_password_endpoint.update_user_password(
        user_id=user_id,
        payload={"password": NEW_VALID_PASS}
    )
    # Assertions
    update_user_password_endpoint.check_that_status_is(404)
    update_user_password_endpoint.check_user_not_found_message(user_id=user_id)


@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[
        (data[1], data[2]) for data in INVALID_HEADERS
    ],
    ids=[title[0] for title in INVALID_HEADERS]
)
def test_update_user_password_with_invalid_headers(
        register_user_endpoint: CreateUser,
        update_user_password_endpoint: UpdateUserPass,
        login_endpoint: Login,
        headers: dict[str, str],
        message: str,
) -> None:
    register_user_endpoint.register_new_user(payload=VALID_CREDENTIALS)
    user_id = register_user_endpoint.user_id

    update_user_password_endpoint.update_user_password(
        user_id=user_id,
        payload={"password": NEW_VALID_PASS},
        headers=headers
    )
    # Assertions
    update_user_password_endpoint.check_that_status_is(401)
    update_user_password_endpoint.check_user_response_body_is_correct(
        expected_message=message
    )
    # check that password was NOT updated
    login_endpoint.login(
        payload={
            "username": VALID_CREDENTIALS["username"],
            "password": NEW_VALID_PASS
        }
    )
    login_endpoint.check_that_status_is(
        error_message="Login with password failed. Returned status code:",
        code=401
    )


@pytest.mark.negative
def test_update_user_password_without_admin_rights(
        login_endpoint: Login,
        register_user_endpoint: CreateUser,
        update_user_password_endpoint: UpdateUserPass
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
    headers = login_endpoint.headers

    update_user_password_endpoint.update_user_password(
        user_id=user_id,
        payload={"password": VALID_CREDENTIALS["password"]},
        headers=headers
    )
    # Assertions
    update_user_password_endpoint.check_that_status_is(403)
    update_user_password_endpoint.check_user_response_body_is_correct(
        expected_message=HEADERS_MESSAGES["no_permissions"]
    )
    # check that password was NOT updated
    login_endpoint.login(
        payload={
            "username": VALID_CREDENTIALS["username"],
            "password": NEW_VALID_PASS
        }
    )
    login_endpoint.check_that_status_is(
        error_message="Login with password failed. Returned status code:",
        code=401
    )
