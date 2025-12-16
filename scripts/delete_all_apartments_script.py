import json
import os

import requests
import dotenv

dotenv.load_dotenv()

URL = os.getenv("BASE_URL")


def get_token(username: str, password: str) -> str:
    token_file = os.getenv("token_file")
    auth_url = f"{URL}/users/login"
    check_url = f"{URL}/users/me"
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


def delete_all_apartments():
    # get headers
    headers = {
        "Authorization": "Bearer " + get_token(
            username=os.getenv("ADMIN_USERNAME"),
            password=os.getenv("ADMIN_PASSWORD")
        )
    }

    # send get request to fetch all apartments ID
    response = requests.get(
        url=f"{URL}/apartments",
        headers=headers,
    )

    # print each response
    print("RESPONSE CODE => ", response.status_code)
    response_json = response.json()
    print("RESPONSE JSON => ", response_json)
    apartment_ids = []
    for apartment in response_json:
        apartment_id = apartment["id"]
        print("APARTMENT_ID => ", apartment_id)
        apartment_ids.append(apartment_id)

    # send delete request to delete apartment
    for apartment_id in apartment_ids:
        response = requests.delete(
            url=f"{URL}/apartments/{apartment_id}",
            headers=headers,
        )
        print("RESPONSE CODE => ", response.status_code)
        print("RESPONSE MESSAGE => ", response.json()["message"])


if __name__ == "__main__":
    delete_all_apartments()
