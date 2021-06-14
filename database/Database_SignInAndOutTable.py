import pymysql

class Database_SignInAndOutTable():

    # database demo to store image in MySQL RDBMS
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                                          user="root", password="Jo(zrju&k6#Z", database="python", charset="utf8")
        self.cursor = self.connection.cursor()


    # create table
    def create_SignInAndOut_table(self):
        sql = "create table if not exists SignInAndOutTable (id int primary key auto_increment,staff_name varchar(20),Time_In varchar(25),Time_Out varchar(25) default(' '));"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except pymysql.Error:
            print(pymysql.Error)


    def insert_signIn(self,name,time):

        sql = 'insert into SignInAndOutTable (staff_name,Time_In) values (%s,%s) '
        self.cursor.execute(sql,(name,time))
        self.connection.commit()


    def insert_signOut(self, name, time):
        #  由名字获取id,插入签退时间
        sql = 'select id from SignInAndOutTable where staff_name = %s'
        self.cursor.execute(sql, name)
        id = self.cursor.fetchone()[0]

        sql = 'update SignInAndOutTable set Time_Out=(%s) where id=(%s) '
        self.cursor.execute(sql,(time,id))
        self.connection.commit()


    def get_allInfo(self):
        datalist = []
        sql = 'select * from SignInAndOutTable'
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

    database = Database_SignInAndOutTable()

    database.create_SignInAndOut_table()

    database.insert_signIn("张三","2021-6-2-20:09")

    database.insert_signOut("张三","2021-6-2-21:09")

    datalist = database.get_allInfo()
    # 遍历列表
    for data in datalist:
        print(data)