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
import pandas as pd

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
            return render_template('login_fail.html')


@app.route('/login_fail', methods=['POST'])
def login_fail():
    return render_template('login_fail.html')


@app.route('/jump_to_login', methods=['POST'])
def jump_to_login():
    if request.method == 'POST':
        return render_template('login.html')


@app.route('/jump_to_register', methods=['POST'])
def jump_to_register():
    if request.method == 'POST':
        return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        print("id", id)
        print("name", password)
        if DatabaseManager().register(id, password):
            return render_template('register_success.html')
        else:
            return render_template('register_fail.html')


@app.route('/signIn')
def signIn():
    return render_template('faceSignIn.html')


@app.route('/signOut')
def signOut():
    return render_template('faceSignOut.html')


@app.route('/updateLib')
def updateLib():
    return render_template('updateLib.html')


@app.route('/videoFaceRecognition')
def videoFaceRecognition():
    return render_template('videoFaceRecognition.html')


@app.route('/addFace')
def addFace():
    return render_template('addFace.html')


@app.route('/statistics')
def statictis():
    # DatabaseTime().__init__()
    result = DatabaseTime().get_allInfo()
    result1 = result[0][0]
    result2 = result[0][1]
    result3 = result[0][2]
    result4 = result[0][3]
    result5 = result[1][0]
    result6 = result[1][1]
    result7 = result[1][2]
    result8 = result[1][3]
    result9 = result[2][0]
    result10 = result[2][1]
    result11 = result[2][2]
    result12 = result[2][3]

    return render_template('statistics.html', result1=result1, result2=result2, result3=result3, result4=result4,
                           result5=result5, result6=result6, result7=result7, result8=result8, result9=result9,
                           result10=result10, result11=result11, result12=result12)


@app.route('/video_match')
def video_match():
    if request.method == 'POST':
        list1 = []
        f = request.files['file']
        video_path = 'static/buffer/video.mp4'
        f.save(video_path)
        cap = cv2.VideoCapture(video_path)
        while True:
            flag, frame = cap.read()
            print('flag:', flag, 'frame.shape:', frame.shape)
            if not flag:
                break
            else:
                list1.append(video_match(frame))
        print(list1)


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
            if identificationCode == -1:
                return render_template('faceSignFail.html')
            else:
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
            return render_template('faceSignFail.html')


@app.route('/faceSignOut', methods=['POST'])
def faceSignOut():
    if request.method == "POST":
        data = request.data.decode('utf-8')
        # print("data:", data)
        json_data = json.loads(data)
        str_image = json_data.get("imgData")
        img = base64.b64decode(str_image)
        img_np = numpy.frombuffer(img, dtype='uint8')
        new_img_np = cv2.imdecode(img_np, 1)
        img_path = './static/buffer/signOutFace.jpg'
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


@app.route('/faceSignOutSuccess', methods=['POST'])
def faceSignOutSuccess():
    if request.method == "POST":
        identificationCode = pic_match('./trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
                                       './static/buffer/signOutFace.jpg')
        if identificationCode:
            if identificationCode == -1:
                return render_template('faceSignFail.html')
            else:
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
            return render_template('faceSignFail.html')


# @app.route('/faceSignInSuccess', methods=['POST'])
# def faceSignInSuccess():
#     if request.method == "POST":
#         data = request.data.decode('utf-8')
#         # print("data:", data)
#         json_data = json.loads(data)
#         str_image = json_data.get("imgData")
#         img = base64.b64decode(str_image)
#         img_np = numpy.frombuffer(img, dtype='uint8')
#         new_img_np = cv2.imdecode(img_np, 1)
#         cv2.imwrite('./static/buffer/signInFace.jpg', new_img_np)
#         print('data:{}'.format('success'))
#     return Response('upload')


@app.route('/video_sample/')
def video_sample():
    return render_template('camera.html')


@app.route('/nothing/')
def nothing():
    return render_template('nothing_here.html')


#
# @app.route('/receiveImage/', methods=["POST"])
# def receive_image():
#     if request.method == "POST":
#         data = request.data.decode('utf-8')
#         # print("data:", data)
#         json_data = json.loads(data)
#         str_image = json_data.get("imgData")
#         img = base64.b64decode(str_image)
#         img_np = numpy.frombuffer(img, dtype='uint8')
#         new_img_np = cv2.imdecode(img_np, 1)
#         cv2.imwrite('./static/buffer/rev_image.jpg', new_img_np)
#         print('data:{}'.format('success'))
#
#     return Response('upload')


#
# @app.route('/addFaceSuccess', methods=['POST'])
# def addFaceSuccess():
#     if request.method == 'POST':
#         buffer_path = 'static/buffer/'
#         f = request.files['file']
#         # print("type(f)", type(f))
#         img_full_path = 'static/buffer/' + f.filename
#         # print("img_path:", img_full_path)
#         f.save(img_full_path)
#
#         identificationCode = match('../faceDemo/trainer.yml', '../faceDemo/haarcascade_frontalface_default.xml',
#                                    img_full_path)
#
#         id = request.form.get('id')
#         name = request.form.get('name')
#         Database().insert_image(id, name, buffer_path, f.filename)
#         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         return render_template('addFaceSuccess.html', id=id, name=name)
@app.route('/addFaceSuccess/', methods=["POST"])
def addFaceSuccess():
    if request.method == "POST":
        data = request.data.decode('utf-8')
        # print("data:", data)
        json_data = json.loads(data)
        str_image = json_data.get("imgData")
        img = base64.b64decode(str_image)
        img_np = numpy.frombuffer(img, dtype='uint8')
        new_img_np = cv2.imdecode(img_np, 1)
        cv2.imwrite('./static/buffer/rev_image.jpg', new_img_np)
        print('data:{}'.format('success'))
    return Response('upload')


@app.route('/addInfoSuccess', methods=['POST'])
def addInfoSuccess():
    if request.method == 'POST':
        buffer_path = 'static/buffer/'
        id1 = request.form.get('id1')
        name1 = request.form.get('name1')
        print("id1", id1)
        print("name1", name1)
        name_in_db = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", DatabasePic().get_name(str(id1)))
        if name_in_db == 'None' or name_in_db == name1:
            DatabasePic().insert_image(id1, name1, buffer_path, 'rev_image.jpg')
            # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return render_template('addFaceSuccess.html', id1=id1, name1=name1)
        else:
            return render_template('addFaceFail.html')


@app.route('/updateLibSuccess', methods=['POST'])
def updateLibSuccess():
    if request.method == 'POST':
        DatabasePic().get_images(r'../pics')
        path = '../pics'
        # 获取图像数组和id标签数组
        faces, ids = getImageAndLabels(path)
        # 获取训练对象
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))
        # 保存文件
        recognizer.write('./trainer.yml')
        return render_template('updateLibSuccess.html')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True, port=5000)
