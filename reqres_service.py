from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone

app = FastAPI()
user_id = 2


@app.get("/api/users/{user_id}")
def get_user():
    return {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }


@app.post(f"/api/users", status_code=201)
def post_user(user_data: dict):
    return {
        "name": user_data.get("name"),
        "job": user_data.get("job"),
        "id": "971",
        "createdAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    }


@app.post("/api/login")
def login_successful(user_data: dict):
    if user_data.get("email") != "eve.holt@reqres.in" or user_data.get("password") != "cityslicka":
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {
        "token": "QpwL5tke4Pnpja7X4"
    }


@app.put("/api/users/{user_id}")
def update_user(user_data: dict):
    return {
    "name": user_data.get("name"),
    "job": user_data.get("job"),
    "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8002)
