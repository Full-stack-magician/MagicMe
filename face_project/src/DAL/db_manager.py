import pymysql


class DatabaseManager():

    # database demo to store image in MySQL RDBMS
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                                          user="root", password="pyh903903", database="python", charset="utf8")
        self.cursor = self.connection.cursor()

    # create table to store imag
    def create_Manager_table(self):
        sql = "create table if not exists managerTable (uid int primary key not null,upword varchar(25) not null);"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except pymysql.Error:
            print(pymysql.Error)

    def register(self, id, pword):

        sql = 'select * from managerTable where uid=%s'  # 查询id是否已经存在,存在则不能注册
        self.cursor.execute(sql, id)
        result = self.cursor.fetchone()

        if result is None:  # 如果匹配不到，就执行注册账号
            sql = 'insert into managerTable (uid,upword) values (%s,%s)'
            self.cursor.execute(sql, (id, pword))
            self.connection.commit()
            return True
        else:
            return False

    def login_verify(self, id, pword):

        sql = "select upword from managerTable where uid = %s"
        self.cursor.execute(sql, id)
        result = self.cursor.fetchone()
        # pword =

        if result is None:  # result为None说明找不到用户名
            return False

        elif result[0] == str(pword):  # 匹配密码
            return True

        else:
            print(type(result[0]), type(pword))
            return False

    # destruction method
    def __del__(self):
        self.connection.close()
        self.cursor.close()


if __name__ == "__main__":
    database = DatabaseManager()

    database.create_Manager_table()

    database.register(110, 111)

    database.login_verify(110, 111)
