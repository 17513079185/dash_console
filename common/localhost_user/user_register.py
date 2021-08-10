from hashlib import sha1
from ckeditor_demo.settings import SECRET_KEY
from db.mysql.ini import DBHandler
import datetime
import re



class UserRegister:

    async def resgister(self, user_name, password, phone, email):
        db = DBHandler()
        # sql = f"""select * from user where username='{user_name}'"""
        sql = f"""select * from user """
        Sqlerr = db.query(sql, one=False)

        is_user = await UserRegister.is_username(Sqlerr, user_name, phone, email)

        if is_user is False:
            return {"msg": "注册信息重复", 'code': 402}

        date = datetime.datetime.now()

        make_password = await UserRegister.make_password(password)  # 加密函数

        sql = f"""insert into `user`(`username`,`password`,`phone`,`email`, `level`, `createtime`) values (%s,%s,%s,%s,%s,%s)"""

        is_null = await UserRegister.is_UserNull(user_name, password, phone, email)

        if is_null:
            return is_null

        Sqlerr = db.insert(sql, ({user_name}, {make_password}, {phone}, {email}, 1, date))

        return {'msg': "注册成功", 'code': 10000}

    async def is_username(Sqlerr, user_name, phone, email):

        try:
            for i in Sqlerr:
                if i['username'] == user_name or i['phone'] == phone or i['email'] == email:
                    return False
        except IOError as e:
            print(e)
        else:
            return True

    async def is_UserNull(user_name, password, phone, email):

        if user_name == None:
            return {'msg': '用户名不得为Null', 'code': 403}

        if not re.match(r'1[3,4,5,7,8,9]\d{9}', phone):
            return {'msg': '手机号格式不对', 'code': 402}

        ex_email = re.compile(r'^[1-9][0-9]{4,10}@qq\.com')
        if not ex_email.match(email):
            return {'msg': '邮箱格式不对,仅限QQ邮箱', 'code': 401}

    async def make_password(password):
        # 1.加盐,SECRET_KEY为加盐字符串,from ads.settings import SECRET_KEY
        password = SECRET_KEY + password
        # 2.开始加密
        sha1_obj = sha1()
        sha1_obj.update(password.encode())
        ret = sha1_obj.hexdigest()

        return ret
