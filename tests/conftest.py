import os

import dotenv
import pytest

@pytest.fixture(scope="session", autouse=True)
def envs():
    """
    Читает все переменные окружения из .env и положит их в переменные текущего запуска/процесса
    """
    dotenv.load_dotenv()

@pytest.fixture(scope="session")
def app_url():
    """
    Фикстура, которая возвращает значение APP_URL из переменных окружения
    """
    return os.getenv("APP_URL")