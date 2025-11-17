import pytest_asyncio
import os
import dotenv

from collections.abc import AsyncGenerator
from httpx import AsyncClient
from pytest import FixtureRequest

from test_data.user_test_parameters import VALID_USER_DATA_LIST
from test_data.apartment_test_data import APARTMENTS_DATA
from test_data.apartment_test_data_tools import get_apartment_data
from test_data.apartment_filtration_test_data import (
    APARTMENT_DATA_FOR_FILTRATION_TEST
)

from tests_async.endpoints.root import HomePage

from tests_async.endpoints.apartment_create import CreateApartment
from tests_async.endpoints.apartment_delete import DeleteApartment
from tests_async.endpoints.apartment_filter import FilterApartments
from tests_async.endpoints.apartment_update import UpdateApartment
from tests_async.endpoints.apartment_retreive import RetrieveApartment
from tests_async.endpoints.apartment_retreive_all import RetrieveAllApartments
from tests_async.endpoints.apartment_upload_plan import UploadApartmentPlan

from tests_async.endpoints.user_create import CreateUser
from tests_async.endpoints.user_delete import DeleteUser
from tests_async.endpoints.user_login import Login
from tests_async.endpoints.user_me import Me
from tests_async.endpoints.user_password import UpdateUserPass
from tests_async.endpoints.user_retrieve import RetrieveUser
from tests_async.endpoints.user_retrieve_all import RetrieveAllUsers

dotenv.load_dotenv()


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """
    Async client for testing an external API.
    """
    async with AsyncClient(
        base_url=os.getenv("BASE_URL")
    ) as client:
        yield client


@pytest_asyncio.fixture
async def home_page_endpoint(async_client: AsyncClient) -> HomePage:
    """
    Fixture that provides access to the home page endpoint.
    """
    return HomePage(async_client)


# ------------------- Apartment Fixtures -------------------

@pytest_asyncio.fixture
async def create_apartment_endpoint(
        async_client: AsyncClient
) -> CreateApartment:
    """
    Fixture that provides access to the apartment creation endpoint.
    """
    return CreateApartment(async_client)


@pytest_asyncio.fixture
async def retrieve_apartments_endpoint(
        async_client: AsyncClient
) -> RetrieveAllApartments:
    """
    Fixture to interact with the endpoint for retrieving all apartments.
    """
    return RetrieveAllApartments(async_client)


@pytest_asyncio.fixture
async def retrieve_apartment_endpoint(
        async_client: AsyncClient
) -> RetrieveApartment:
    """
    Fixture that provides access to the endpoint for retrieving a single
    apartment.
    """
    return RetrieveApartment(async_client)


@pytest_asyncio.fixture
async def filter_apartment_endpoint(
        async_client: AsyncClient
) -> FilterApartments:
    """
    Fixture that provides access to the apartment filtering endpoint.
    """
    return FilterApartments(async_client)


@pytest_asyncio.fixture
async def update_apartment_endpoint(
        async_client: AsyncClient
) -> UpdateApartment:
    """
    Fixture that provides access to the apartment update endpoint.
    """
    return UpdateApartment(async_client)


@pytest_asyncio.fixture
async def delete_apartment_endpoint(
        async_client: AsyncClient
) -> DeleteApartment:
    """
    Fixture that provides access to the apartment deletion endpoint.
    """
    return DeleteApartment(async_client)


@pytest_asyncio.fixture
async def create_few_apartments(
        delete_apartment_endpoint: DeleteApartment,
        async_client: AsyncClient
) -> AsyncGenerator[int, None]:
    """
    Fixture that creates multiple apartments before a test and deletes
    them afterward.

    Yields:
        int: Number of created apartments.
    """
    new_apartments = []
    for apartments_data in APARTMENTS_DATA:
        new_apartment = CreateApartment(async_client)
        await new_apartment.create_apartment(payload=apartments_data)
        new_apartments.append(new_apartment)

    yield len(new_apartments)

    for new_apartment in new_apartments:
        await delete_apartment_endpoint.delete_apartment_by_id(
            new_apartment.apartment_id
        )


@pytest_asyncio.fixture
async def create_few_specific_apartments(
        delete_apartment_endpoint: DeleteApartment,
        async_client: AsyncClient,
) -> AsyncGenerator[list[CreateApartment], None]:
    """
    Fixture that creates a specific set of apartments for filtration tests and
    deletes them afterward.

    Yields:
        list[CreateApartment]: List of created apartment objects.
    """
    new_apartments = []
    for apartments_data in APARTMENT_DATA_FOR_FILTRATION_TEST:
        new_apartment = CreateApartment(async_client)
        await new_apartment.create_apartment(payload=apartments_data)
        new_apartments.append(new_apartment)

    yield new_apartments

    for new_apartment in new_apartments:
        await delete_apartment_endpoint.delete_apartment_by_id(
            new_apartment.apartment_id
        )


@pytest_asyncio.fixture
async def create_two_apartments_for_duplicate_test(
        delete_apartment_endpoint: DeleteApartment,
        async_client: AsyncClient,
) -> AsyncGenerator[tuple[int, int, int], None]:
    """
    Fixture that creates two apartments with the same `unit_id` for
    duplicate-checking tests.

    Yields:
        tuple: (first_apartment_id, second_apartment_id,
                first_apartment_unit_id)
    """
    apartment_valid_data1 = get_apartment_data()
    apartment_valid_data2 = get_apartment_data()

    new_apartment1 = CreateApartment(async_client)
    await new_apartment1.create_apartment(payload=apartment_valid_data1)

    new_apartment2 = CreateApartment(async_client)
    await new_apartment2.create_apartment(payload=apartment_valid_data2)

    first_apartment_id = new_apartment1.apartment_id
    second_apartment_id = new_apartment2.apartment_id
    first_apartment_unit_id = apartment_valid_data1["unit_id"]

    yield (
        first_apartment_id, second_apartment_id, first_apartment_unit_id
    )
    await delete_apartment_endpoint.delete_apartment_by_id(first_apartment_id)
    await delete_apartment_endpoint.delete_apartment_by_id(second_apartment_id)


@pytest_asyncio.fixture(autouse=True)
async def cleanup_apartment(
        request: FixtureRequest,
        create_apartment_endpoint: CreateApartment,
        delete_apartment_endpoint: DeleteApartment
) -> None:
    """
    Autouse fixture that deletes the created apartment after each test if
    it exists.
    """
    try:
        yield
    finally:
        apartment_id = create_apartment_endpoint.apartment_id
        if apartment_id is not None:
            await delete_apartment_endpoint.delete_apartment_by_id(
                apartment_id
            )


@pytest_asyncio.fixture
async def upload_plan_endpoint(
        async_client: AsyncClient
) -> UploadApartmentPlan:
    """
    Fixture that provides access to the apartment plan upload endpoint.

    Returns:
        UploadApartmentPlan: Helper class for uploading floor plan images
        for a given apartment.
    """
    return UploadApartmentPlan(async_client)


# ------------------- User Fixtures -------------------

@pytest_asyncio.fixture
async def login_endpoint(async_client: AsyncClient) -> Login:
    """
    Fixture that provides access to the user login endpoint.
    """
    return Login(async_client)


@pytest_asyncio.fixture
async def me_endpoint(async_client: AsyncClient) -> Me:
    """
    Fixture that provides access to the `/me` user info endpoint.
    """
    return Me(async_client)


@pytest_asyncio.fixture
async def register_user_endpoint(async_client: AsyncClient) -> CreateUser:
    """
    Fixture that provides access to the user registration endpoint.
    """
    return CreateUser(async_client)


@pytest_asyncio.fixture
async def retrieve_user_endpoint(async_client: AsyncClient) -> RetrieveUser:
    """
    Fixture that provides access to the endpoint for retrieving a single user.
    """
    return RetrieveUser(async_client)


@pytest_asyncio.fixture
async def retrieve_users_endpoint(
        async_client: AsyncClient
) -> RetrieveAllUsers:
    """
    Fixture that provides access to the endpoint for retrieving all users.
    """
    return RetrieveAllUsers(async_client)


@pytest_asyncio.fixture
async def update_user_password_endpoint(
        async_client: AsyncClient
) -> UpdateUserPass:
    """
    Fixture that provides access to the user password update endpoint.
    """
    return UpdateUserPass(async_client)


@pytest_asyncio.fixture
async def delete_user_endpoint(async_client: AsyncClient) -> DeleteUser:
    """
    Fixture that provides access to the user deletion endpoint.
    """
    return DeleteUser(async_client)


@pytest_asyncio.fixture
async def create_few_users(
        delete_user_endpoint: DeleteUser,
        async_client: AsyncClient
) -> AsyncGenerator[list[CreateUser], None]:
    """
    Fixture that creates multiple users before a test and deletes them
    afterward.

    Yields:
        list[CreateUser]: List of created user objects.
    """
    new_users: list[CreateUser] = []
    for users_data in VALID_USER_DATA_LIST:
        new_user = CreateUser(async_client)
        await new_user.register_new_user(payload=users_data[1])
        new_users.append(new_user)

    yield new_users

    for new_user in new_users:
        await delete_user_endpoint.delete_user_by_id(new_user.user_id)


@pytest_asyncio.fixture(autouse=True)
async def cleanup_user(
        request: FixtureRequest,
        register_user_endpoint: CreateUser,
        delete_user_endpoint: DeleteUser
) -> None:
    """
    Autouse fixture that deletes the created user after each test if it exists.
    """
    try:
        yield
    finally:
        user_id = register_user_endpoint.user_id
        if user_id is not None:
            await delete_user_endpoint.delete_user_by_id(user_id)
