from app.models.User import User
from config import Server
from clients.base_session import BaseSession


class ApiClient:
    def __init__(self, **kwargs):
        env = kwargs.pop("env")
        self.session = BaseSession(base_url=Server(env).service)

    def get_user(self, user_id):
        response = self.session.get(f"/api/users/{user_id}")

        return response

    def get_users(self):
        response = self.session.get(f"/api/users/")
        return response

    def create_user(self, user_data):
        response = self.session.post(f"/api/users", json=user_data)
        return response

    def delete_user(self, user_id):
        response = self.session.delete(f"/api/users/{user_id}")
        return response

    def update_user(self, user_id, update_data):

        response = self.session.patch(f"/api/users/{user_id}", json=update_data)
        return response