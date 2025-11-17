import json
import os
import dotenv
from httpx import AsyncClient

dotenv.load_dotenv()


async def get_valid_token(
        async_client: AsyncClient,
        username: str,
        password: str
) -> str:
    """
    Asynchronously retrieve a valid authentication token for the given user.

    First, attempts to load a cached token from a local JSON file and validate
    it via the /users/me endpoint.

    If the token is missing or invalid, performs a login request to
    /users/login using the provided credentials. The new token is cached
    for future reuse.

    Args:
        async_client (AsyncClient): The HTTP client used to perform requests.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        str: A valid access token.

    Raises:
        Exception: If a valid token could not be obtained.
    """
    token_file = os.getenv("token_file")
    auth_url = "/users/login"
    check_url = "/users/me"
    auth_payload = {"username": username, "password": password}

    data = {}  # Dictionary to store 'username': 'token' pairs

    # If the file with the token exists, read the token
    if os.path.exists(token_file):
        with open(token_file, "r") as file:
            data = json.load(file)

    # If the username already has a token, check its validity
    if username in data:
        token = data[username]
        response = await async_client.get(
            check_url,
            headers={"Authorization": f"Bearer {token}"}
        )
        if response.status_code == 200:
            return token  # Return valid token

    # If the file does not exist or the token is invalid, request a new token
    response = await async_client.post(auth_url, json=auth_payload)

    if response.status_code == 200:
        token = response.json().get("access_token")
        if token:
            data[username] = token  # Update the dictionary with the new token
            with open(token_file, "w") as file:
                json.dump(data, file, indent=4)  # Save updated tokens to file
            return token

    # If all attempts fail, raise an exception
    raise Exception("Failed to get a valid token")
