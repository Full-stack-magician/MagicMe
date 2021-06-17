import cv2 as cv

image = cv.imread("./pics/555.webp")
print(image.shape)
# image = cv.resize(image, dsize=(600, 560))
# image = cv.resize(image1, dsize=(1200, 560))
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face_detector = cv.CascadeClassifier("D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
faces = face_detector.detectMultiScale(image, 1.01, 25)
for x, y, w, h in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), color=(0, 0, 255))
cv.imshow('input', image)
cv.waitKey(0)
