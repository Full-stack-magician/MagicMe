import os
import cv2
import sys
from PIL import Image
import numpy as np
import re


def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 检测人脸
    face_detector = cv2.CascadeClassifier(
        'D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')

    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片
        PIL_img = Image.open(imagePath).convert('L')
        # 将图像转换为数组
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id
        # id = int(os.path.split(imagePath)[1].split('.')[0])

        str1 = re.findall(r'\d+', os.path.split(imagePath)[1].split('-')[0])
        list1 = ''
        for str2 in str1:
            list1 = list1 + str2
        id = int(list1)

        print("id", id)
        print("os.path.split(imagePath)[1]", os.path.split(imagePath)[1])
        # id= re.findall(r'\d+', imagePath)[0]
        for x, y, w, h in faces:
            facesSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
            print("ids", ids)
    return facesSamples, ids


if __name__ == '__main__':
    # 图片路径
    path = './picsForTrain/'
    # 获取图像数组和id标签数组
    faces, ids = getImageAndLabels(path)
    # 获取训练对象
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('./trainer.yml')
