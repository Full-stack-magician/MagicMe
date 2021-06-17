import pymysql
from src.DAL.db_pic import *


class DatabaseTime():

    # database demo to store image in MySQL RDBMS
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                                          user="root", password="pyh903903", database="python", charset="utf8")
        self.cursor = self.connection.cursor()

    # create table
    def create_SignInAndOut_table(self):
        sql = "create table if not exists SignInAndOutTable (id int primary key ,staff_name varchar(20),Time_In varchar(25),Time_Out varchar(25) default(' '));"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except pymysql.Error:
            print(pymysql.Error)

    def insert_signIn(self, id, name, time):
        sql_select = 'select * from SignInAndOutTable where id=%s'  # 查询id是否已经存在,存在则不能注册
        self.cursor.execute(sql_select, id)
        result = self.cursor.fetchone()
        if result:
            return False
        else:
            sql = 'insert into SignInAndOutTable (id,staff_name,Time_In) values (%s,%s,%s) '
            self.cursor.execute(sql, (id, name, time))
            self.connection.commit()
            return True

    def insert_signOut(self, name, time):
        # #  由名字获取id,插入签退时间
        # sql_select = 'select id from pictures where s_name = %s'
        # print("sql_select", sql_select)
        # DatabasePic().cursor.execute(sql_select, name+'1')
        # id = DatabasePic().cursor.fetchone()[0]
        # print("id from picture", id)
        # sql = 'update SignInAndOutTable set Time_Out=(%s) where id=(%s) '
        # self.cursor.execute(sql, (time, id))
        # self.connection.commit()
        # if id:
        #     return True
        # else:
        #     return False
        sql_select = 'select id from SignInAndOutTable where staff_name = %s'
        print("sql_select", sql_select)
        self.cursor.execute(sql_select, name)
        id = self.cursor.fetchone()
        print("id", id)
        if id is not None:
            sql = 'update SignInAndOutTable set Time_Out=(%s) where id=(%s) '
            self.cursor.execute(sql, (time, id))
            self.connection.commit()
            return True
        else:
            return False

    def get_allInfo(self):
        datalist = []
        sql = 'select * from SignInAndOutTable ORDER BY id DESC'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for i in result:
            datalist.append(i)
        return datalist

    # destruction method
    def __del__(self):
        self.connection.close()
        self.cursor.close()


if __name__ == "__main__":

    database = DatabaseTime()

    database.create_SignInAndOut_table()

    database.insert_signIn("张三", "2021-6-2-20:09")

    database.insert_signOut("张三", "2021-6-2-21:09")

    datalist = database.get_allInfo()
    # 遍历列表
    for data in datalist:
        print(data)
