import allure
import pytest

from typing import Dict

from tests.endpoints.user_login import Login
from test_data.user_test_parameters import INVALID_CREDENTIALS_TESTS_PARAM
from test_data.user_test_data import (
    TEST_USERNAME,
    TEST_PASS,
)


@allure.story("Positive")
@pytest.mark.smoke
@pytest.mark.positive
def test_login(login_endpoint: Login) -> None:
    login_endpoint.login(
        payload={
            "username": TEST_USERNAME,
            "password": TEST_PASS
        }
    )
    login_endpoint.check_that_status_is(200)
    login_endpoint.check_that_field_type_is(
        field="access_token",
        expected_type=str
    )
    login_endpoint.check_that_field_type_is(
        field="token_type",
        expected_type=str
    )
    login_endpoint.check_that_field_equals(
        field="token_type",
        expected_value="bearer"
    )


@allure.story("Negative")
@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="payload, message, status_code",
    argvalues=[
        (data[1], data[2], data[3]) for data in INVALID_CREDENTIALS_TESTS_PARAM
    ],
    ids=[title[0] for title in INVALID_CREDENTIALS_TESTS_PARAM]
)
def test_login_with_invalid_data(
        login_endpoint: Login,
        payload: Dict,
        message: str,
        status_code: int
) -> None:
    login_endpoint.login(payload)
    # Assertions
    login_endpoint.check_that_status_is(status_code)
    login_endpoint.check_error_response_body_is_correct(
        expected_message=message
    )
