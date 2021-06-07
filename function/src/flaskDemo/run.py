from flask import Flask, render_template, request, Response
from src.faceDemo.pic_match import pic_match
from src.faceDemo.video_match import video_match
import time
from src.DAL.db_pic import *
from src.DAL.db_time import *
from src.DAL.db_manager import *
from src.faceDemo.dataTrain import *
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

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def index11():
    return render_template('login.html')


@app.route('/haha')
def index():
    return 'haha'


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        if DatabaseManager().login_verify(str(id), password):
            return render_template('index.html')
        else:
            return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        print("id", id)
        print("name", password)
        if DatabaseManager().register(id, password):
            return render_template('login.html')
        else:
            return "账号已存在"


@app.route('/signIn')
def signIn():
    return render_template('faceSignIn.html')


@app.route('/signOut')
def signOut():
    return render_template('faceSignOut.html')


@app.route('/updateLib')
def updateLib():
    return render_template('updateLib.html')






# @app.route('/faceSignInSuccess', methods=['POST'])
# def faceSignInSuccess():
#     if request.method == 'POST':
#         f = request.files['file']
#         img_path = 'static/buffer/signInFace.jpg'
#         # print("img_path", img_path)
#         # print("ftype", type(f))
#         f.save(img_path)
#         identificationCode = match('../faceDemo/trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
#                                    img_path)
#         id = request.form.get('id')
#         name = request.form.get('name')
#         # print('name:', name)
#         # print('password:', id)
#         # img_path = './/' + str(id) + '.jpg'
#         # print("img_path", img_path)
#         if 10 <= identificationCode < 30:
#             result = '成龙'
#         elif 30 <= identificationCode < 50:
#             result = '懂王'
#         elif 80 <= identificationCode <= 82:
#             result = '彭于晏'
#         return render_template('faceSignInSuccess.html', result=result)
@app.route('/faceSignIn', methods=['POST'])
def faceSignIn():
    if request.method == "POST":
        data = request.data.decode('utf-8')
        # print("data:", data)
        json_data = json.loads(data)
        str_image = json_data.get("imgData")
        img = base64.b64decode(str_image)
        img_np = numpy.frombuffer(img, dtype='uint8')
        new_img_np = cv2.imdecode(img_np, 1)
        img_path = './static/buffer/signInFace.jpg'
        cv2.imwrite(img_path, new_img_np)
        # identificationCode = match('./trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
        #                            img_path)
        # # sql = "SELECT s_name from pictures where id = " + str(identificationCode)
        # # Database().cursor.execute(sql)
        # # print("Database().cursor.execute(sql)", Database().cursor.execute(sql))
        # print("identificationCode", identificationCode)
        # print("Database().cursor.execute(sql)", Database().get_name(str(identificationCode)))
        # result = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", Database().get_name(str(identificationCode)))
        # print('result:', result)
        return "hh"
    # return Response('upload')


@app.route('/faceSignInSuccess', methods=['POST'])
def faceSignInSuccess():
    if request.method == "POST":
        identificationCode = pic_match('./trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
                                       './static/buffer/signInFace.jpg')
        if identificationCode:
            # sql = "SELECT s_name from pictures where id = " + str(identificationCode)
            # Database().cursor.execute(sql)
            # print("Database().cursor.execute(sql)", Database().cursor.execute(sql))
            print("identificationCode", identificationCode)
            print("Database().cursor.execute(sql)", DatabasePic().get_name(str(identificationCode)))
            result = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", DatabasePic().get_name(str(identificationCode)))
            print('resultSignIn:', result)

            sign_in_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if DatabaseTime().insert_signIn(identificationCode, result, sign_in_time):
                return render_template('faceSignInSuccess.html', result=result)
            else:
                return render_template('faceSignInSuccess.html', result=result + ' 已经签到了，别签了')
        else:
            return "未检测到有效人脸！"





@app.route('/faceSignOutSuccess', methods=['POST'])
def faceSignOutSuccess():
    if request.method == "POST":
        identificationCode = pic_match('./trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
                                       './static/buffer/signOutFace.jpg')
        if identificationCode:
            # sql = "SELECT s_name from pictures where id = " + str(identificationCode)
            # Database().cursor.execute(sql)
            # print("Database().cursor.execute(sql)", Database().cursor.execute(sql))
            print("identificationCode", identificationCode)
            print("Database().cursor.execute(sql)", DatabasePic().get_name(str(identificationCode)))
            result = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", DatabasePic().get_name(str(identificationCode)))
            print('resultSignOut:', result)

            sign_out_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if DatabaseTime().insert_signOut(result, sign_out_time):
                return render_template('faceSignOutSuccess.html', result=result)
            else:
                return render_template('faceSignOutSuccess.html', result=result + '   今天还没签到！')
        else:
            return "未检测到有效人脸！"







if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True, port=5000)
