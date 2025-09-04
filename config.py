import os


class Server:
    def __init__(self, env):
        self.service = {
            "dev": os.getenv("APP_URL"),
            "rc": ""
        }[env]