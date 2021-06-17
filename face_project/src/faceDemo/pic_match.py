import cv2
from PIL import Image


def pic_match(matchLibAddress, cascadeClassifierAddress, picAddress):
    # 加载训练数据集文件
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    recogizer.read(matchLibAddress)
    # 准备识别的图片
    img = cv2.imread(picAddress)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(
        cascadeClassifierAddress)
    faces = face_detector.detectMultiScale(gray)
    result = {}
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        # 人脸识别
        id, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        # print('标签id:', id, '置信评分：', confidence)
        # cv2.imshow('result', cv2.resize(img, dsize=(400, 500)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print("confidence", confidence)
        if confidence > 50:
            return -1
        else:
            cv2.imwrite('./static/buffer/' + 'show' + '.jpg', img)
            return id


def pic_match_for_video(matchLibAddress, cascadeClassifierAddress, img):
    # 加载训练数据集文件
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    recogizer.read(matchLibAddress)
    # 准备识别的图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(
        cascadeClassifierAddress)
    faces = face_detector.detectMultiScale(gray)
    result = {}
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        # 人脸识别
        id, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        # print('标签id:', id, '置信评分：', confidence)
        # cv2.imshow('result', cv2.resize(img, dsize=(400, 500)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print("confidence", confidence)
        cv2.imwrite('./static/buffer/' + 'show' + '.jpg', img)
        print("id", id)
        cv2.imshow('result', img)
        return id
