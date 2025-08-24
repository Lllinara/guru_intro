# from http import HTTPStatus
# import pytest
# import requests
# def test_service_availability_by_users(app_url):
#     response = requests.get(f"{app_url}/status")
#     assert response.json()["users"]
#
# def test_service_http_status(app_url):
#     response = requests.get(f"{app_url}/status")
#     assert response.status_code == HTTPStatus.OK
#
# def test_service_response_time(app_url):
#     response = requests.get(f"{app_url}/status")
#     response_time = response.elapsed.total_seconds()
#
#     assert response_time < 0.1, f"Слишком медленный ответ: {response_time:.3f}s"
