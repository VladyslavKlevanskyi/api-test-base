import pytest
from tests.endpoints.root import HomePage


@pytest.mark.smoke
def test_home_page_status_code_and_message(
        home_page_endpoint: HomePage
) -> None:
    home_page_endpoint.open()
    # Assertions
    home_page_endpoint.check_that_status_is(200)
    home_page_endpoint.check_response_message("Home Page")
