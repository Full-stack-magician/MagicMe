import cv2
from PIL import Image
from src.faceDemo.pic_match import *


def video_match(matchLibAddress, cascadeClassifierAddress):
    #cap = cv2.VideoCapture(r'E:\qqCache\1464002726\FileRecv\MobileFile\video_20210603_145128.mp4')
    #cap = cv2.VideoCapture(r'E:\qqCache\1464002726\FileRecv\MobileFile\video_20210603_151249.mp4')
    cap = cv2.VideoCapture(r'E:\qqCache\1464002726\FileRecv\MobileFile\video_20210603_151906.mp4')

    while True:
        flag, frame = cap.read()
        print('flag:', flag, 'frame.shape:', frame.shape)
        if not flag:
            break
        pic_match_for_video(matchLibAddress, cascadeClassifierAddress, frame)
        if ord('q') == cv2.waitKey(10):
            break
    cv2.destroyAllWindows()
    cap.release()
