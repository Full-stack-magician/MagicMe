from flask import Flask, render_template, request, Response
from src.faceDemo.pic_match import pic_match
import time
from src.DAL.db_pic import *
from src.DAL.db_time import *
from src.DAL.db_manager import *
from src.faceDemo.dataTrain import *
from src.faceDemo.video_match import *
import os
import cv2
import json
import sys
from PIL import Image
import numpy as np
import re
import numpy
import base64
from flask_cors import CORS

# Database().insert_images(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\pics')
# print(type(database.select_count_by_name("成龙")))
# file = open(os.path.join(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\test', '10-成龙.jpg'), 'rb')
# image = file.read()
# Database().insert_image(14, '成龙', image)
# Database().get_images(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\test')

# path = '../pics'
# # 获取图像数组和id标签数组
# faces, ids = getImageAndLabels(path)
# # 获取训练对象
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.train(faces, np.array(ids))
# # 保存文件
# recognizer.write('./trainer.yml')

# print("Database().cursor.execute(sql)", Database().get_name(str(1)))
# identificationCode = match(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\flaskDemo\trainer.yml',
#                            r'E:\Hchier\pythonProjects3.9.4\faceTest\src\faceDemo\haarcascade_frontalface_default.xml',
#                            r'E:\Hchier\pythonProjects3.9.4\faceTest\src\flaskDemo\static\buffer\signInFace.jpg')
# print(identificationCode)


# Database_SignInAndOut().create_SignInAndOut_table()

# # Database_SignInAndOut().insert_signIn('1', 'jack', '200')
# Database_SignInAndOut().insert_signOut('jack', '300')
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# Database_ManagerTable().create_Manager_table()
# Database_ManagerTable().register('1', '11')
# print(Database_ManagerTable().login_verify('1', '11'))

# sql = 'select id from pictures where s_name = %s'
# DatabaseTime().__init__()
# DatabaseTime().cursor.execute(sql, '裴宇航1')
# id = DatabaseTime().cursor.fetchone()[0]
# print(id)
# DatabaseTime().__init__()
# print(DatabaseTime().get_allInfo())


# video_match(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\flaskDemo\trainer.yml'
#             , '../faceDemo/haarcascade_frontalface_default.xml')
# print(pic_match(r'E:\Hchier\pythonProjects3.9.4\faceTest\src\flaskDemo\trainer.yml'
#                           , '../faceDemo/haarcascade_frontalface_default.xml',
#                           r'E:\Hchier\pythonProjects3.9.4\faceTest\src\pics\3-pyh5.jpg'))

print(re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", DatabasePic().get_name(str(5))))