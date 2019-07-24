# coding=utf-8
import numpy as np
import cv2 as cv

# 创建300*512三通道的黑色图片
img = np.zeros((300, 512, 3), np.uint8)
# 窗口名字为"image"
winName = "image"
cv.namedWindow(winName)

# 创建开关
switch = '0 : OFF \n1 : ON'


# 教程中nothing为空，动手改了一下。
def nothing(x):
    # 得到trackbars滑块的值
    r = cv.getTrackbarPos('R', winName)
    g = cv.getTrackbarPos('G', winName)
    b = cv.getTrackbarPos('B', winName)
    s = cv.getTrackbarPos(switch, winName)
    # 如果开关为0，则图片显示为黑色
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    pass
    cv.imshow('image', img)


if __name__ == '__main__':
    cv.imshow('image', img)

    # 创建trackbars滑块
    cv.createTrackbar('R', winName, 0, 255, nothing)
    cv.createTrackbar('G', winName, 0, 255, nothing)
    cv.createTrackbar('B', winName, 0, 255, nothing)
    cv.createTrackbar(switch, winName, 0, 1, nothing)

    nothing(0)
    cv.waitKey(0)
    cv.destroyAllWindows()
---------------------
作者：TanKimko
来源：CSDN
原文：https: // blog.csdn.net / tankimko / article / details / 80019410
版权声明：本文为博主原创文章，转载请附上博文链接！