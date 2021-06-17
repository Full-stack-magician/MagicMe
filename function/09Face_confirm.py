import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
#加载训练数据集文件

def cv2ImgAddText(img, text, left, top, textColor="red", textSize=40):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')
#准备识别的图片
name=["彭于晏","欧豪"]
#print(name[0])
#print(name[1])
img=cv2.imread('data/test/5.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(
    'D:\Anaconda3\lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
faces = face_detector.detectMultiScale(gray)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #人脸识别
    id,confidence=recogizer.predict(gray[y:y+h,x:x+w])
    if id>=1|id<=12:
        print('标签id:', id, '置信评分：', confidence)
        img = cv2ImgAddText(img, name[0], 10, 65, "red", 40)
    else:
        print('标签id:', id, '置信评分：', confidence)
        img = cv2ImgAddText(img, name[1], 10, 65, "red", 40)
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()