from urllib.request import Request
from venv import logger

from ckeditor_demo.settings import SECRET_KEY
from fastapi import FastAPI, Form
from starlette.responses import JSONResponse
from common.computetime import Computetime
from common.localhost_user.user_login import login
from common.localhost_user.user_register import UserRegister
import time
import jwt
import uvicorn

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

    login_url = str(request.url)[22:]
    register_url = str(request.url)[22:]

    if login_url == 'login_user' or register_url == 'register_user':  # 屏蔽注册、登录接口, 避免死循环
        return response

    try:
        token = request.headers['token']  # 获取前端传过来token
        jwt.decode(token, key=SECRET_KEY)

    except Exception as e:
        logger.warning(e)
        return JSONResponse({'msg': 'token验证失败,请重新登陆!', 'code': 301})

    return response


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8008, reload=True, debug=True)
