#导入模块
import cv2 as cv
#读取图片
#img=cv.imread('所要读取的图片所在的地址')
img=cv.imread('testphoto\pyy4.png') #路径中不能有中文，否则加载图片失败
#显示图片
cv.imshow('read_img',img)
#等待键盘输入 单位毫秒  传入0 则就是无限等待
cv.waitKey(3000)
#释放内存  由于OpenCV底层是C++编写的,所以需要将图片暂时占用的缓存空间释放
cv.destroyAllWindows()