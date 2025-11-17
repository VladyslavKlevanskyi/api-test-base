import os
from dotenv import load_dotenv

from test_data.user_test_data import (
    random_valid_user_credentials,
    TEST_PASS,
    TEST_USERNAME,
    get_few_random_user_data,
    USERS_NUMBER
)
from test_data.user_test_data_messages import USER_MASSAGES

load_dotenv()

# Valid user data for boundary positive user creation test
BOUNDARY_VALUES_TESTS_PARAM = [
    (
        "Username 3 chars",
        {
            "username": "New",
            "password": random_valid_user_credentials()["password"]
        }
    ),
    (
        "Username 20 chars",
        {
            "username": "Te" * 10,
            "password": random_valid_user_credentials()["password"]
        }
    ),
    (
        "Password 8 chars",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "Pass-_!1"
        }
    ),
    (
        "Password 256 chars",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "Tp$1" * 64
        }
    )
]

# List of random valid user credentials
VALID_USER_DATA_LIST = get_few_random_user_data(times=USERS_NUMBER)

# List of random valid user credentials with boundary values
VALID_CREDENTIALS_LIST = BOUNDARY_VALUES_TESTS_PARAM + VALID_USER_DATA_LIST

# Invalid data for login
INVALID_CREDENTIALS_TESTS_PARAM = [
    ("Empty payload", {}, USER_MASSAGES["Field_required"], 422),
    ("Payload is None", None, USER_MASSAGES["Field_required"], 422),
    # username field
    (
        "Invalid username",
        {
            "username": "AnyName",
            "password": TEST_PASS
        },
        USER_MASSAGES["invalid_credentials"],
        401
    ),
    (
        "No username field in payload",
        {
            "password": TEST_PASS
        },
        USER_MASSAGES["Field_required"],
        422
    ),
    (
        "Username is a None",
        {
            "username": None,
            "password": TEST_PASS
        },
        USER_MASSAGES["Valid_string"],
        422
    ),
    (
        "Username is an empty string",
        {
            "username": "",
            "password": TEST_PASS
        },
        USER_MASSAGES["less_3_char"],
        422
    ),
    (
        "Username is less then 3 characters",
        {
            "username": "Te",
            "password": TEST_PASS
        },
        USER_MASSAGES["less_3_char"],
        422
    ),
    (
        "Username is more then 20 characters",
        {
            "username": "T" * 21,
            "password": TEST_PASS
        },
        USER_MASSAGES["more_20_char"],
        422
    ),
    (
        "Username with @#$!&?* % symbols and spaces",
        {
            "username": "@#$!&?* %",
            "password": TEST_PASS
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    (
        "Username with ~`^\"\':;?,./| symbols",
        {
            "username": "~`^\"\':;?,./|",
            "password": TEST_PASS
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    (
        "Username with (){}[]<> symbols",
        {
            "username": "(){}[]<>",
            "password": TEST_PASS
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    # password field
    (
        "Invalid password",
        {
            "username": TEST_USERNAME,
            "password": "AnyPass_1#"
        },
        USER_MASSAGES["invalid_credentials"],
        401
    ),

    (
        "No password field in payload",
        {
            "username": TEST_USERNAME,
        },
        USER_MASSAGES["Field_required"],
        422
    ),
    (
        "Password is a None",
        {
            "username": TEST_USERNAME,
            "password": None
        },
        USER_MASSAGES["Valid_string"],
        422
    ),
    (
        "Password is an empty string",
        {
            "username": TEST_USERNAME,
            "password": ""
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is less then 8 characters",
        {
            "username": TEST_USERNAME,
            "password": "TestPas"
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is more then 256 characters",
        {
            "username": TEST_USERNAME,
            "password": "T" * 257
        },
        USER_MASSAGES["more_256_char"],
        422
    ),
    (
        "Password with non-Latin letters",
        {
            "username": TEST_USERNAME,
            "password": "яЖбЮфΩδتشکगघ"
        },
        USER_MASSAGES["pass_value_error"],
        422
    ),
    (
        "Password without lowercase letter",
        {
            "username": TEST_USERNAME,
            "password": "33WEGSDV#_1"
        },
        USER_MASSAGES["pass_lowercase"],
        422
    ),
    (
        "Password without uppercase letter",
        {
            "username": TEST_USERNAME,
            "password": "33wesdsd#_1"
        },
        USER_MASSAGES["pass_uppercase"],
        422
    ),
    (
        "Password without digit",
        {
            "username": TEST_USERNAME,
            "password": "RRwesdsd123"
        },
        USER_MASSAGES["pass_special"],
        422
    ),
]

#  Invalid data for user creation
INVALID_DATA_TESTS_PARAM = [
    ("Empty payload", {}, USER_MASSAGES["Field_required"], 422),
    ("Payload is None", None, USER_MASSAGES["Field_required"], 422),
    # username field
    (
        "No username field in payload",
        {
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["Field_required"],
        422
    ),
    (
        "Username is a None",
        {
            "username": None,
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["Valid_string"],
        422
    ),

    (
        "Username is an empty string",
        {
            "username": "",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["less_3_char"],
        422
    ),
    (
        "Username is less then 3 characters",
        {
            "username": "Te",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["less_3_char"],
        422
    ),
    (
        "Username is more then 20 characters",
        {
            "username": "T" * 21,
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["more_20_char"],
        422
    ),
    (
        "Username as a string of 5 spaces",
        {
            "username": "     ",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    (
        "Username with @#$!&?* % symbols and spaces",
        {
            "username": "@#$!&?* %",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    (
        "Username with ~`^\"\':;?,./| symbols",
        {
            "username": "~`^\"\':;?,./|",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    (
        "Username with (){}[]<> symbols",
        {
            "username": "(){}[]<>",
            "password": random_valid_user_credentials()["password"]
        },
        USER_MASSAGES["username_value_error"],
        422
    ),
    # password field
    (
        "No password field in payload",
        {
            "username": random_valid_user_credentials()["username"],
        },
        USER_MASSAGES["Field_required"],
        422
    ),
    (
        "Password is a None",
        {
            "username": random_valid_user_credentials()["username"],
            "password": None
        },
        USER_MASSAGES["Valid_string"],
        422
    ),
    (
        "Password is an empty string",
        {
            "username": random_valid_user_credentials()["username"],
            "password": ""
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is less then 8 characters",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "TestPas"
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is more then 256 characters",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "T" * 257
        },
        USER_MASSAGES["more_256_char"],
        422
    ),
    (
        "Password as a string of 9 spaces",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "         "
        },
        USER_MASSAGES["pass_value_error"],
        422
    ),
    (
        "Password with non-Latin letters",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "яЖбЮфΩδتشکगघ"
        },
        USER_MASSAGES["pass_value_error"],
        422
    ),
    (
        "Password without lowercase letter",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "33WEGSDV#_1"
        },
        USER_MASSAGES["pass_lowercase"],
        422
    ),
    (
        "Password without uppercase letter",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "33wesdsd#_1"
        },
        USER_MASSAGES["pass_uppercase"],
        422
    ),
    (
        "Password without digit",
        {
            "username": random_valid_user_credentials()["username"],
            "password": "RRwesdsd123"
        },
        USER_MASSAGES["pass_special"],
        422
    ),
]

INVALID_PASS_FIELD_TESTS_PARAM = [
    (
        "empty payload",
        {},
        USER_MASSAGES["Field_required"],
        422
    ),
    (
        "Password is a None",
        {
            "password": None
        },
        USER_MASSAGES["Valid_string"],
        422
    ),
    (
        "Password is an empty string",
        {
            "password": ""
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is less then 8 characters",
        {
            "password": "TestPas"
        },
        USER_MASSAGES["less_8_char"],
        422
    ),
    (
        "Password is more then 256 characters",
        {
            "password": "T" * 257
        },
        USER_MASSAGES["more_256_char"],
        422
    ),
    (
        "Password as a string of 9 spaces",
        {
            "password": "         "
        },
        USER_MASSAGES["pass_value_error"],
        422
    ),
    (
        "Password with non-Latin letters",
        {
            "password": "яЖбЮфΩδتشکगघ"
        },
        USER_MASSAGES["pass_value_error"],
        422
    ),
    (
        "Password without lowercase letter",
        {
            "password": "33WEGSDV#_1"
        },
        USER_MASSAGES["pass_lowercase"],
        422
    ),
    (
        "Password without uppercase letter",
        {
            "password": "33wesdsd#_1"
        },
        USER_MASSAGES["pass_uppercase"],
        422
    ),
    (
        "Password without digit",
        {
            "password": "RRwesdsd123"
        },
        USER_MASSAGES["pass_special"],
        422
    ),
]

INVALID_AUTHORIZATION_TESTS_PARAM = [
    (
        "Headers is empty",
        {},
        "Not authenticated"
    ),
    (
        "Authorization is an empty string",
        {"Authorization": ""},
        "Not authenticated"
    ),
    (
        "Token is empty",
        {"Authorization": "Bearer"},
        "Could not validate credentials"
    ),
    (
        "Invalid token",
        {"Authorization": f"Bearer {os.getenv('invalid_token')}"},
        "Could not validate credentials"
    ),
]
