import pytest

from collections.abc import Generator
from pytest import FixtureRequest


from test_data.apartment_test_data import APARTMENTS_DATA
from test_data.apartment_test_data_tools import get_apartment_data
from test_data.apartment_filtration_test_data import (
    APARTMENT_DATA_FOR_FILTRATION_TEST
)

from tests_sync.endpoints.root import HomePage

from tests_sync.endpoints.apartment_create import CreateApartment
from tests_sync.endpoints.apartment_delete import DeleteApartment
from tests_sync.endpoints.apartment_filter import FilterApartments
from tests_sync.endpoints.apartment_update import UpdateApartment
from tests_sync.endpoints.apartment_retreive import RetrieveApartment
from tests_sync.endpoints.apartment_retreive_all import RetrieveAllApartments
from tests_sync.endpoints.apartment_upload_plan import UploadApartmentPlan

from test_data.user_test_parameters import VALID_USER_DATA_LIST
from tests_sync.endpoints.user_create import CreateUser
from tests_sync.endpoints.user_delete import DeleteUser
from tests_sync.endpoints.user_login import Login
from tests_sync.endpoints.user_me import Me
from tests_sync.endpoints.user_password import UpdateUserPass
from tests_sync.endpoints.user_retrieve import RetrieveUser
from tests_sync.endpoints.user_retrieve_all import RetrieveAllUsers



@pytest.fixture
def home_page_endpoint() -> HomePage:
    """
    Fixture that provides access to the home page endpoint methods.
    """
    return HomePage()


# ------------------- Apartment Fixtures -------------------

@pytest.fixture
def create_apartment_endpoint() -> CreateApartment:
    """
    Fixture to interact with the apartment creation endpoint.
    """
    return CreateApartment()


@pytest.fixture
def retrieve_apartments_endpoint() -> RetrieveAllApartments:
    """
    Fixture to interact with the endpoint for retrieving all apartments.
    """
    return RetrieveAllApartments()


@pytest.fixture
def retrieve_apartment_endpoint() -> RetrieveApartment:
    """
    Fixture to interact with the endpoint for retrieving a single apartment.
    """
    return RetrieveApartment()


@pytest.fixture
def filter_apartment_endpoint() -> FilterApartments:
    """
    Fixture that provides access to the apartment filtering endpoint.
    """
    return FilterApartments()


@pytest.fixture
def update_apartment_endpoint() -> UpdateApartment:
    """
    Fixture that provides access to the apartment update endpoint.
    """
    return UpdateApartment()


@pytest.fixture
def delete_apartment_endpoint() -> DeleteApartment:
    """
    Fixture that provides access to the apartment deletion endpoint.
    """
    return DeleteApartment()


@pytest.fixture
def create_few_apartments(
        delete_apartment_endpoint: DeleteApartment,
) -> Generator[int, None, None]:
    """
    Fixture that creates multiple apartments before a test and deletes
    them afterward.

    Yields:
        int: Number of created apartments.
    """
    new_apartments = []
    for apartments_data in APARTMENTS_DATA:
        new_apartment = CreateApartment()
        new_apartment.create_apartment(payload=apartments_data)
        new_apartments.append(new_apartment)

    yield len(new_apartments)

    for new_apartment in new_apartments:
        delete_apartment_endpoint.delete_apartment_by_id(
            new_apartment.apartment_id
        )


@pytest.fixture
def create_few_specific_apartments(
        delete_apartment_endpoint: DeleteApartment,
) -> Generator[list[CreateApartment], None, None]:
    """
    Fixture that creates a specific set of apartments for filtration tests
    and deletes them afterward.

    Yields:
        list[CreateApartment]: List of created apartment objects.
    """
    new_apartments = []
    for apartments_data in APARTMENT_DATA_FOR_FILTRATION_TEST:
        new_apartment = CreateApartment()
        new_apartment.create_apartment(payload=apartments_data)
        new_apartments.append(new_apartment)

    yield new_apartments

    for new_apartment in new_apartments:
        delete_apartment_endpoint.delete_apartment_by_id(
            new_apartment.apartment_id
        )


@pytest.fixture
def create_two_apartments_for_duplicate_test(
        delete_apartment_endpoint: DeleteApartment,
) -> Generator[tuple[int, int, int], None, None]:
    """
    Fixture that creates two apartments with the same `unit_id` for
    duplicate-checking tests.

    Yields:
        tuple: (first_apartment_id, second_apartment_id,
        first_apartment_unit_id)
    """
    apartment_valid_data1 = get_apartment_data()
    apartment_valid_data2 = get_apartment_data()

    new_apartment1 = CreateApartment()
    new_apartment1.create_apartment(payload=apartment_valid_data1)

    new_apartment2 = CreateApartment()
    new_apartment2.create_apartment(payload=apartment_valid_data2)

    first_apartment_id = new_apartment1.apartment_id
    second_apartment_id = new_apartment2.apartment_id
    first_apartment_unit_id = apartment_valid_data1["unit_id"]

    yield (
        first_apartment_id, second_apartment_id, first_apartment_unit_id
    )
    delete_apartment_endpoint.delete_apartment_by_id(first_apartment_id)
    delete_apartment_endpoint.delete_apartment_by_id(second_apartment_id)


@pytest.fixture
def upload_plan_endpoint() -> UploadApartmentPlan:
    """
    Fixture that provides access to the apartment plan upload endpoint.

    Returns:
        UploadApartmentPlan: Helper class for uploading floor plan images
        for a given apartment.
    """
    return UploadApartmentPlan()


@pytest.fixture(autouse=True)
def cleanup_apartment(
        request: FixtureRequest,
        create_apartment_endpoint: CreateApartment,
        delete_apartment_endpoint: DeleteApartment
) -> None:
    """
    Autouse fixture that automatically deletes the apartment created
    during a test.

    Called after each test using a finalizer.
    """
    def delete_apartment() -> None:
        apartment_id = create_apartment_endpoint.apartment_id
        delete_apartment_endpoint.delete_apartment_by_id(apartment_id)

    request.addfinalizer(delete_apartment)


# ------------------- User Fixtures -------------------

@pytest.fixture
def login_endpoint() -> Login:
    """
    Fixture to interact with the user login endpoint.
    """
    return Login()


@pytest.fixture
def me_endpoint() -> Me:
    """
    Fixture to interact with the `/me` user info endpoint.
    """
    return Me()


@pytest.fixture
def register_user_endpoint() -> CreateUser:
    """
    Fixture to interact with the user registration endpoint.
    """
    return CreateUser()


@pytest.fixture
def retrieve_user_endpoint() -> RetrieveUser:
    """
    Fixture that provides access to the endpoint for retrieving a
    single user.
    """
    return RetrieveUser()


@pytest.fixture
def retrieve_users_endpoint() -> RetrieveAllUsers:
    """
    Fixture that provides access to the endpoint for retrieving all users.
    """
    return RetrieveAllUsers()


@pytest.fixture
def update_user_password_endpoint() -> UpdateUserPass:
    """
    Fixture that provides access to the user password update endpoint.
    """
    return UpdateUserPass()


@pytest.fixture
def delete_user_endpoint() -> DeleteUser:
    """
    Fixture that provides access to the user deletion endpoint.
    """
    return DeleteUser()


@pytest.fixture
def create_few_users(
        delete_user_endpoint: DeleteUser
) -> Generator[list[CreateUser], None, None]:
    """
    Fixture that creates several users before a test and deletes them
    afterward.

    Yields:
        list[CreateUser]: List of created user objects.
    """
    new_users: list[CreateUser] = []
    for users_data in VALID_USER_DATA_LIST:
        new_user = CreateUser()
        new_user.register_new_user(payload=users_data[1])
        new_users.append(new_user)

    yield new_users

    for new_user in new_users:
        delete_user_endpoint.delete_user_by_id(new_user.user_id)


@pytest.fixture(autouse=True)
def cleanup_user(
        request: FixtureRequest,
        register_user_endpoint: CreateUser,
        delete_user_endpoint: DeleteUser
) -> None:
    """
    Autouse fixture that automatically deletes the user created during a test.

    Called after each test using a finalizer.
    """
    def delete_user() -> None:
        user_id = register_user_endpoint.user_id
        delete_user_endpoint.delete_user_by_id(user_id)

    request.addfinalizer(delete_user)
