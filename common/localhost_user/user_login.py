from ckeditor_demo.settings import SECRET_KEY
from common.localhost_user.user_register import UserRegister
from db.mysql.ini import DBHandler
import jwt
import datetime


async def login(user_name, password):
    password = await UserRegister.make_password(password)

    db = DBHandler()
    sql = f"""select * from user where username='{user_name}' and password='{password}'"""
    Sqlerr = db.query(sql, one=False)

    if Sqlerr:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            'uid': Sqlerr[0]['id'],
        }

        token = jwt.encode(payload=payload, key=SECRET_KEY)

        return {'msg': '登录成功', 'code': '10000', 'token': token, 'user_name': Sqlerr[0]['username']}

    return {'msg': '账号或密码错误!', 'code': '10001'}
