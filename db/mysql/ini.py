import pymysql


class DBHandler:
    def __init__(self, host='127.0.0.1', port=3306, user='root', password='123456',
                 database='fastapi', charset='utf8', **kwargs):
        # 连接数据库服务器
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                    database=database, cursorclass=pymysql.cursors.DictCursor,
                                    charset=charset, **kwargs)
        # 获取游标
        self.cursor = self.conn.cursor()

    # 查询单表所有
    def query(self, sql, args=None, one=True):

        self.cursor.execute(sql, args)
        # 提交事务
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    # 插入单条数据
    def insert(self, sql, args=None):

        try:
            data = self.cursor.execute(sql, args)
            self.conn.commit()

            return data
        except IOError as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()
