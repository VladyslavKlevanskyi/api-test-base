import pytest
from tests_async.endpoints.root import HomePage


@pytest.mark.asyncio
async def test_home_page_status_code_and_message(
        home_page_endpoint: HomePage
) -> None:
    await home_page_endpoint.open()
    # Assertions
    home_page_endpoint.check_that_status_is(200)
    home_page_endpoint.check_response_message("Home Page")
