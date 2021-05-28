import cv2 as cv
img=cv.imread('testphoto\pyy4.png')
cv.imshow('img',img)
print('原来图片的形状',img.shape)
# resize_img=cv.resize(img,dsize=(200,240,4))
resize_img=cv.resize(img,dsize=(1000,397*2))
print('修改后图片的形状：',resize_img.shape)
cv.imshow('resize_img',resize_img)

cv.waitKey(100)
#只有输入q时候，退出
while True:
    if ord('q')==cv.waitKey(0):
        break

cv.destroyAllWindows()
