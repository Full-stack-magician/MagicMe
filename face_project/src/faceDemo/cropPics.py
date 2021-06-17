import cv2 as cv

for i in range(30, 50):
    i_temp = i
    img = cv.imread('./picsForTrain/' + str(i) + '.jpg')
    print(img.shape)
    face_detector = cv.CascadeClassifier(
        "D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(img, 1.01, 25)
    for x, y, w, h in faces:
        cropped = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
        cv.imwrite('./picsForTrain/' + str(i_temp) + '.jpg', cropped)
