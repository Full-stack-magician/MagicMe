import pymysql


class Database():

    def __init__(self):
        self.connection = pymysql.connect(host="localhost",
                        user="root", password="Jo(zrju&k6#Z", database="python", charset="utf8")
        self.cursor = self.connection.cursor()


    def create_image_table(self):
        sql = 'create table if not exists picture ( \
                image longblob);'

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except pymysql.Error:
            print(pymysql.Error)


    def insert_image(self, image):
        sql = "insert into picture(image) values(%s)"
        self.cursor.execute(sql, image)
        self.connection.commit()


    def get_image(self, path):
        sql = 'select * from picture'
        try:
            self.cursor.execute(sql)
            image = self.cursor.fetchone()[0]
            with open(path, "wb") as file:
                file.write(image)
        except pymysql.Error:
            print(pymysql.Error)
        except IOError:
            print(IOError)


    def __del__(self):
        self.connection.close()
        self.cursor.close()


if __name__ == "__main__":
    database = Database()
    # read image from current directory
    with open("./1.png", "rb") as file:
        image = file.read()

    database.create_image_table()
    database.insert_image(image)

    database.get_image('./result.jpg')
