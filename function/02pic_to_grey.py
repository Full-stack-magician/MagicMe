import cv2 as cv
img=cv.imread('lena.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# cv.waitKey(0)
#只有输入q时候，退出
while True:
    if ord('q')==cv.waitKey(0):
        break

cv.destroyAllWindows()
