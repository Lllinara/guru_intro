import json
import uvicorn
from http import HTTPStatus
from fastapi import FastAPI
from fastapi_pagination import Page, add_pagination, paginate
from datetime import datetime, timezone
from models.User import User
from models.AppStatus import AppStatus

app = FastAPI()
add_pagination(app)
users: list[User] = []
@app.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(users=bool(users))

@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    return users[user_id - 1]

@app.get("/api/users", status_code=HTTPStatus.OK)
def get_users() -> Page[User]:
    return paginate(users)



#
# @app.get("/api/users/{user_id}")
# def get_user():
#     return {
#         "data": {
#             "id": 2,
#             "email": "janet.weaver@reqres.in",
#             "first_name": "Janet",
#             "last_name": "Weaver",
#             "avatar": "https://reqres.in/img/faces/2-image.jpg"
#         },
#         "support": {
#             "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
#             "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
#         }
#     }
#
#
# @app.post(f"/api/users", status_code=201)
# def post_user(user_data: dict):
#     return {
#         "name": user_data.get("name"),
#         "job": user_data.get("job"),
#         "id": "971",
#         "createdAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
#     }
#
#
# @app.post("/api/login")
# def login_successful(user_data: dict):
#     if user_data.get("email") != "eve.holt@reqres.in" or user_data.get("password") != "cityslicka":
#         raise HTTPException(status_code=400, detail="Invalid email or password")
#     return {
#         "token": "QpwL5tke4Pnpja7X4"
#     }
#
#
# @app.put("/api/users/{user_id}")
# def update_user(user_data: dict):
#     return {
#     "name": user_data.get("name"),
#     "job": user_data.get("job"),
#     "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
# }


if __name__ == "__main__":
    with open("users.json") as f:
        users = json.load(f)

    for user in users:
        User.model_validate(user)
    print("Users loaded")
    uvicorn.run(app, host="0.0.0.0", port=8002)
