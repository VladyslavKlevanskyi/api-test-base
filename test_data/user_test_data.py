import os
import random
from dotenv import load_dotenv

from typing import List, Dict, Tuple
from faker import Faker

load_dotenv()

fake = Faker()

TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASS = os.getenv("TEST_PASS")

USERS_NUMBER = 5  # number of generated users for tests_users


def random_valid_user_credentials() -> dict[str, str]:
    """
    Returns a dictionary with valid credentials for a user.
    """
    # Create random username
    username = (
        f"{fake.first_name()}{random.choice('_-')}"
        f"{random.randint(1, 100)}"
    )
    # Create random password
    password = (
        f"{fake.last_name()}"
        f"{''.join(random.choices('~!@#$%^&*_-', k=3))}"
        f"{random.randint(1, 100)}"
    )
    return {"username": username, "password": password}


def get_few_random_user_data(
        times: int
) -> List[Tuple[str, Dict[str, str]]]:
    user_list = []
    num = 1
    for user in range(times):
        user = random_valid_user_credentials()
        user_list.append((f"Random user credentials {num}", user))
        num += 1
    return user_list


VALID_CREDENTIALS = random_valid_user_credentials()
NEW_VALID_PASS = random_valid_user_credentials()["password"]
