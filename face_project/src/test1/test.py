import re

# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def show(self):
#         print("age", self.age, "name", self.age)
#
#
# if __name__ == '__main__':
#     person1 = Person(10, "jack")
#     person2 = Person(11, "mike")
#     person1.show()
#     person2.show()


# str1 = "1dfafawf而我国为423 .223、33t"
# str1 = re.sub(r"\d", "", str)
# print(str1)
import re
string = "hello,world!!%[545]你好234asd完全额。。。"
str = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", string)
print(str)