# coding=utf-8
import numpy as np
import cv2

# 创建300*512三通道的黑色图片
img = np.zeros((300, 512, 3), np.uint8)

# # 窗口名字
winName = "Controller"
cv2.namedWindow(winName)
# 创建开关
switch = '0on1off'
# 教程中nothing为空，动手改了一下。
def nothing(x):
    # 得到trackbars滑块的值
    r = cv2.getTrackbarPos('R', winName)
    g = cv2.getTrackbarPos('G', winName)
    b = cv2.getTrackbarPos('B', winName)
    s = cv2.getTrackbarPos(switch, winName)
    # 如果开关为1，则图片显示为黑色
    if s == 1:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    pass
    cv2.imshow('image', img)   #把刚才载入的图片显示出来

if __name__ == '__main__':
    cv2.imshow('image', img)

    # 创建trackbars滑块
    cv2.createTrackbar('R', winName, 0, 255, nothing)
    cv2.createTrackbar('G', winName, 0, 255, nothing)
    cv2.createTrackbar('B', winName, 0, 255, nothing)
    cv2.createTrackbar(switch, winName, 0, 1, nothing)

    nothing(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

