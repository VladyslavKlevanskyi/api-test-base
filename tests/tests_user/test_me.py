import pytest

from typing import Dict

from tests.endpoints.user_me import Me
from test_data.user_test_parameters import INVALID_AUTHORIZATION_TESTS_PARAM


@pytest.mark.positive
def test_me_endpoint(me_endpoint: Me) -> None:
    me_endpoint.open_me()
    me_endpoint.check_that_status_is(200)
    me_endpoint.check_that_field_type_is(field="username", expected_type=str)
    me_endpoint.check_that_field_type_is(field="id", expected_type=int)
    me_endpoint.check_that_field_type_is(field="is_admin", expected_type=bool)


@pytest.mark.smoke
@pytest.mark.negative
@pytest.mark.parametrize(
    argnames="headers, message",
    argvalues=[
        (data[1], data[2]) for data in INVALID_AUTHORIZATION_TESTS_PARAM
    ],
    ids=[title[0] for title in INVALID_AUTHORIZATION_TESTS_PARAM]
)
def test_me_endpoint_with_invalid_data(
        me_endpoint: Me,
        headers: Dict,
        message: str
) -> None:
    me_endpoint.open_me(headers=headers)
    me_endpoint.check_that_status_is(401)
    me_endpoint.check_user_response_body_is_correct(expected_message=message)
