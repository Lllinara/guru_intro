# Микросервис вместо https://reqres.in

Микросервис на **Python + FastAPI**, совместимый с [reqres.in](https://reqres.in/) API.

## Эндпоинты

| Метод | URL | Описание             |
|-------|-----|----------------------|
| `GET` | `/api/users/{user_id}` | Получить пользователя |
| `POST` | `/api/users` | Создать пользователя |
| `PUT` | `/api/users/{user_id}` | Обновить пользователя |
| `POST` | `/api/login` | Авторизация          |

## Запуск

1. **Установить зависимости:**
```bash
pip install fastapi uvicorn requests pytest
```

2. **Запустить сервис:**
```bash
python reqres_service.py
```
Сервис доступен на `http://localhost:8002`

3. **Запустить тесты:**
```bash
pytest test_users.py -v
```


## Файлы

- `reqres-service.py` - основной сервис
- `test_users.py` - автотесты
