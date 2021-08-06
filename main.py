import uvicorn
from fastapi import FastAPI, Form
from common.computetime import Computetime
from common.localhost_user.user_register import UserRegister

app = FastAPI()


@app.get("/datetimecompute")
async def datetimecompute():
    datetime = Computetime().date_days_count()

    return datetime


@app.post("/register_user")
async def register_user(
        user_name: str = Form(None),
        password: str = Form(None),
        phone: str = Form(None),
        email: str = Form(None)
):
    data = await UserRegister.resgister(self=None, user_name=user_name, password=password, phone=phone, email=email)

    return data


@app.post("/login_user")
async def login_user():
    pass

    return True


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8008, reload=True, debug=True)
