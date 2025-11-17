import os

from dotenv import load_dotenv

load_dotenv()


HEADERS_MESSAGES = {
    "not_authenticated": "Not authenticated",
    "no_permissions": "Not enough permissions",
    "not_valid_credentials": "Could not validate credentials",
}

# invalid headers for creation and retrieving tests
INVALID_HEADERS = [
    (
        "No Authorization header",
        {},
        HEADERS_MESSAGES["not_authenticated"],
        401
    ),
    (
        "No token",
        {"Authorization": "Bearer"},
        HEADERS_MESSAGES["not_valid_credentials"],
        401
    ),
    (
        "Authorization header is an empty string",
        {"Authorization": ""},
        HEADERS_MESSAGES["not_authenticated"],
        401
    ),
    (
        "Invalid token",
        {"Authorization": "Bearer " + os.getenv("invalid_token")},
        HEADERS_MESSAGES["not_valid_credentials"],
        401
    )
]
