import json
import math
from http import HTTPStatus
import pytest
import requests
from app.models.User import User


@pytest.fixture(scope="module")
def fill_test_data(app_url):
    with open("users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{app_url}/api/users", json=user)
        a = response.json()
        api_users.append(response.json())
    user_ids = [user["id"] for user in api_users]

    yield user_ids

    for user_id in user_ids:
        requests.delete(f"{app_url}/api/users/{user_id}")





@pytest.fixture
def users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK
    return response.json()

@pytest.mark.usefixtures("fill_test_data")
def test_users(app_url):
    response = requests.get(f"{app_url}/api/users")
    assert response.status_code == HTTPStatus.OK

    user_list = response.json()
    print(user_list)
    for user in user_list:
        User.model_validate(user)

def test_users_no_duplicates(users):
    users_ids = [user["id"] for user in users]
    assert len(users_ids) == len(set(users_ids))



# @pytest.mark.parametrize("user_id", [1, 7, 12])

def test_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.get(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK

        user = response.json()
        User.model_validate(user)

@pytest.mark.parametrize("user_id", [0, 21])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR

@pytest.mark.parametrize("user_id", ["hdh"])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("page, size",[(1,3), (2,3), (4,3)])
def test_users_simple(app_url, users, page, size):
    response = requests.get(f"{app_url}/api/users?page={page}&size={size}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "items" in data
    assert data["total"] == len(users)
    assert data["page"] == page
    assert data["size"] == size
    assert "pages" in data

    expected_pages = math.ceil(len(users) / size)
    if page <= expected_pages:
        if page < expected_pages:
            expected_count = size
        else:
            expected_count = len(users) - size * (expected_pages - 1)
        assert len(data["items"]) == expected_count, f"На странице {page} ожидалось {expected_count} элементов, получено {len(data['items'])}"

    else:
        assert len(data["items"]) == 0, "Несуществующая страница должна возвращать пустой список"


    assert data["pages"] == expected_pages, f"При size={size} ожидалось {expected_pages} страниц, получено {data['pages']}"

@pytest.mark.parametrize("size", [3, 4, 5, 12, 13])
def test_different_data_on_different_pages(app_url, users, size):
    data1 = requests.get(f"{app_url}/api/users?page=1&size={size}").json()
    data2 = requests.get(f"{app_url}/api/users?page=2&size={size}").json()

    if size < len(users):
        user_ids1 = [user["id"] for user in data1['items']]
        user_ids2 = [user["id"] for user in data2['items']]
        assert user_ids1 != user_ids2, "На обеих страницах одинаковые данные"
    else:
        assert len(data2['items']) == 0 and len(data1["items"]) == len(users), "Страница 2 пустая"
