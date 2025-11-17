import json
import os
import dotenv
import requests

dotenv.load_dotenv()


def get_valid_token(base_url: str, username: str, password: str) -> str:
    """
    Retrieve a valid authentication token for the given user.

    Args:
        base_url (str): Base URL for the API endpoints.
        username (str): The username used for authentication.
        password (str): The password used for authentication.

    Returns:
        str: A valid authentication token.

    Raises:
        Exception: If a valid token could not be obtained.
    """
    token_file = os.getenv("TOKEN_FILE")
    auth_url = f"{base_url}users/login"
    check_url = f"{base_url}users/me"
    auth_payload = {"username": username, "password": password}

    data = {}  # Dictionary to store 'username': 'token' pairs

    # If the file with the token exists, read the token
    if os.path.exists(token_file):
        with open(token_file, "r") as file:
            data = json.load(file)

    # If the username already has a token, check its validity
    if username in data:
        token = data[username]
        response = requests.get(
            check_url,
            headers={"Authorization": f"Bearer {token}"}
        )
        if response.status_code == 200:
            return token  # Return valid token

    # If the file does not exist or the token is invalid, request a new token
    response = requests.post(auth_url, json=auth_payload)

    if response.status_code == 200:
        token = response.json().get("access_token")
        if token:
            data[username] = token  # Update the dictionary with the new token
            with open(token_file, "w") as file:
                json.dump(data, file, indent=4)  # Save updated tokens to file
            return token

    # If all attempts fail, raise an exception
    raise Exception("Failed to get a valid token")
