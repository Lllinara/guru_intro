import requests

# API_BASE_URL = "https://reqres.in/api"
API_BASE_URL = "http://0.0.0.0:8002/api"
user_id = 2
headers = {'x-api-key': 'reqres-free-v1'}

def test_user_data():
    # url = "http://0.0.0.0:8002/api/users/2"

    expected_id = 2
    expected_email = "janet.weaver@reqres.in"

    response = requests.get(url=f"{API_BASE_URL}/users/{user_id}", headers=headers)

    actual_data = response.json()["data"]

    assert actual_data["id"] == expected_id
    assert actual_data["email"] == expected_email

def test_create_user():
    name = "morpheus"
    job = "leader"
    response = requests.post(url=f"{API_BASE_URL}/users", json={"name": name, "job": job}, headers=headers)

    assert response.json()["name"] == name
    assert response.status_code == 201

def test_login_successful():
    email = "eve.holt@reqres.in"
    password = "cityslicka"
    expected_token = "QpwL5tke4Pnpja7X4"

    response = requests.post(url=f"{API_BASE_URL}/login", json={"email": email, "password": password}, headers=headers)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
    actual_data = response.json()

    assert 'token' in actual_data
    assert actual_data['token'] == expected_token



def test_update_user():
    name = "morpheus"
    job = "zion resident"

    response = requests.put(url=f"{API_BASE_URL}/users/{user_id}", json={"name": name, "job": job}, headers=headers)

    actual_data = response.json()
    print(actual_data)
    assert 'updatedAt' in actual_data
    assert actual_data["name"] == name
