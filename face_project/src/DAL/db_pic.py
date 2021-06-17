import os
import re
import pymysql


class DatabasePic():

    # database demo to store image in MySQL RDBMS
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                                          user="root", password="pyh903903", database="python", charset="utf8")
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
    def insert_images(self, path):

        path_list = os.listdir(path)

        for filename in path_list:
            file = open(os.path.join(path, filename), 'rb')
            image = file.read()
            # print("imagetype", type(image))
            pattern = r'-'
            filename = filename[0:-4]  # 截取图片.pong的前面部分
            result = re.split(pattern, filename)
            id = int(result[0])
            name = result[1]

            sql = "insert into pictures values(%s,%s,%s)"
            self.cursor.execute(sql, (id, name, image))
            self.connection.commit()

    def insert_image(self, id, name, path, filename):
        # print("insert_image sql")
        file = open(os.path.join(path, filename), 'rb')
        image = file.read()
        sql = "insert into pictures values(%s,%s,%s)"
        rename = name + str(DatabasePic().select_count_by_name(name) + 1)
        self.cursor.execute(sql, (id, rename, image))
        self.connection.commit()

    # def insert_image(self, id, name, image):
    #     print("insert_image sql")
    #     sql = "insert into pictures values(%s,%s,%s)"
    #     rename = name + str(Database().select_count_by_name(name) + 1)
    #     self.cursor.execute(sql, (id, rename, image))
    #     self.connection.commit()

    def select_count_by_name(self, name):
        sql = "select count(s_name) from pictures where s_name like '%" + name + "%' "
        # print(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    # get image from database
    def get_images(self, path):

        sql = 'select * from pictures'
        path1 = path  # 保存根目录的备份,因为后面每一张图片的路径都不一样
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            for i in result:
                path = path1
                id = str(i[0])
                name = i[1]
                image = i[2]
                path = path + "/" + id + "-" + name + ".jpg"
                print(path)
                with open(path, "wb") as file:
                    file.write(image)
        except pymysql.Error:
            print(pymysql.Error)
        except IOError:
            print(IOError)

    # def get_image(self, path):
    #
    #     sql = 'select * from pictures'
    #     path1 = path  # 保存根目录的备份,因为后面每一张图片的路径都不一样
    #     try:
    #         self.cursor.execute(sql)
    #         result = self.cursor.fetchall()
    #         for i in result:
    #             path = path1
    #             id = str(i[0])
    #             name = i[1]
    #             image = i[2]
    #             path = path + "\\" + id + "-" + name + ".jpg"
    #             print(path)
    #             image.save(path + "\id.jpg")
    #     except pymysql.Error:
    #         print(pymysql.Error)
    #     except IOError:
    #         print(IOError)

    # get name by id from database

    def get_name(self, id):
        sql = 'select * from pictures where id=%s'
        try:
            self.cursor.execute(sql, id)
            result = self.cursor.fetchone()
            print(result)
        except pymysql.Error:
            print(pymysql.Error)
        except IOError:
            print(IOError)
        if result:
            return result[1]
        else:
            return 'None'

    # destruction method
    # def __del__(self):
    #     self.connection.close()
    #     self.cursor.close()


if __name__ == "__main__":
    database = DatabasePic()
    #
    # database.create_image_table()
    #
    database.insert_images(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\pics')

    # 从数据库中得到数据  ( r'D:\pic\1.png' )为指定图片存放的位置
    # database.get_image(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\test')

    # id = 1
    # name = database.get_name(id)
