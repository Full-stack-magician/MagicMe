import os
import re
import pymysql

class Database():

    # database demo to store image in MySQL RDBMS
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                        user="root", password="Jo(zrju&k6#Z", database="python", charset="utf8")
        self.cursor = self.connection.cursor()


    # create table to store imag
    def create_image_table(self):
        sql = "create table if not exists pictures (Id int primary key not null,s_name varchar(255) not null,image longblob);"
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except pymysql.Error:
            print(pymysql.Error)


    # insert image into table
    def insert_image(self, path):

        path_list = os.listdir(path)

        for filename in path_list:
            file = open(os.path.join(path, filename), 'rb')
            image = file.read()

            pattern = r'-'
            filename = filename[0:-4]   #截取图片.pong的前面部分
            result = re.split(pattern, filename)
            id = int(result[0])
            name = result[1]

            sql = "insert into pictures values(%s,%s,%s)"
            self.cursor.execute(sql, (id, name, image))
            self.connection.commit()


    # get image from database
    def get_image(self, path):

        sql = 'select * from pictures'
        path1 = path    #保存根目录的备份,因为后面每一张图片的路径都不一样
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                path = path1
                id = str(i[0])
                name = i[1]
                image = i[2]
                path = path+"\\"+id+"-"+name+".jpg"
                print(path)
                with open(path, "wb") as file:
                    file.write(image)
        except pymysql.Error:
            print(pymysql.Error)
        except IOError:
            print(IOError)


    # get name by id from database
    def get_name(self,id):
        sql = 'select * from pictures where id=%s'
        try:
            self.cursor.execute(sql,id)
            result = self.cursor.fetchone()

        except pymysql.Error:
            print(pymysql.Error)
        except IOError:
            print(IOError)
        return result[1]



    # destruction method
    def __del__(self):
        self.connection.close()
        self.cursor.close()



if __name__ == "__main__":

    database = Database()

    database.create_image_table()

    database.insert_image(r'D:\pic')

    # 从数据库中得到数据  ( r'D:\pic\1.png' )为指定图片存放的位置
    database.get_image(r'D:\pic\pic')

    id = 1
    name = database.get_name(id)
