import os
import dotenv
import requests

from tests.auth_tools import get_valid_token

dotenv.load_dotenv()

BASE_URL = os.getenv("BASE_URL")

headers = {
    "Authorization": "Bearer " + get_valid_token(
        base_url=BASE_URL,
        username=os.getenv("ADMIN_USERNAME"),
        password=os.getenv("ADMIN_PASSWORD")
    )
}

payload = {
    "username": os.getenv("TEST_USERNAME"),
    "password": os.getenv("TEST_PASS")
}

result = requests.post(
    url=os.getenv("BASE_URL") + "users/register",
    headers=headers,
    json=payload
)
print(result.status_code)
print(result.json())
