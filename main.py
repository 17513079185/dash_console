import time
from urllib.request import Request

import jwt
import uvicorn
from ckeditor_demo.settings import SECRET_KEY
from fastapi import FastAPI, Form
from common.computetime import Computetime
from common.localhost_user.user_login import login
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
async def login_user(
        user_name: str = Form(None),
        password: str = Form(None)
):
    data = await login(user_name, password)

    return data


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    response = await call_next(request)

    url = str(request.url)[22:]

    if url == 'login_user':  # 屏蔽登录接口, 避免死循环

        return response

    token = request.headers['token']  # 获取前端传过来token
    try:
        e = jwt.decode(token, key=SECRET_KEY)
        print(e)
    except:
        return False

    return response


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8008, reload=True, debug=True)
