import cv2
import numpy as np



def show_rgb(color):

    if color == ord('r'):
        cap = cv2.VideoCapture(0)  # 摄像头实时获取

        while (1):
            ret, frame = cap.read()  # ret 为True 或者False,代表有没有读取到图片  frame表示截取到一帧的图片 （BGR）
            b, g, r = cv2.split(frame)  # 分离BGR三个通道

            #merged = cv2.merge([b, g, r])  # 合并三个通道
            # cv2.imshow("merged 1", merged)    //显示三通道融合图

            # 原始图像
            cv2.imshow('image', frame)
            # 单通道的灰度图
            cv2.imshow("Red 1", r)
            # 单通道的通道合并
            zeros = np.zeros(frame.shape[:2], dtype="uint8")
            merged_r = cv2.merge([zeros, zeros, r])
            cv2.imshow("merged_r", merged_r)


            cv2.waitKey(1)  # 括号内为0时 只取第一张图 ； 为1时实时显示

    elif color == ord('g'):
        while (1):
            ret, frame = cap.read()  # ret 为True 或者False,代表有没有读取到图片  frame表示截取到一帧的图片 （BGR）
            b, g, r = cv2.split(frame)  # 分离BGR三个通道
            merged = cv2.merge([b, g, r])  # 合并三个通道

            # 原始图像
            cv2.imshow('image', frame)
            # 单通道的灰度图
            cv2.imshow("Green 1", g)
            # 单通道的通道合并
            zeros = np.zeros(frame.shape[:2], dtype="uint8")
            merged_r = cv2.merge([zeros, g, zeros])
            cv2.imshow("merged_g", merged_g)

            cv2.waitKey(1)  # 括号内为0时 只取第一张图 ； 为1时实时显示

    else:
        while (1):
            ret, frame = cap.read()  # ret 为True 或者False,代表有没有读取到图片  frame表示截取到一帧的图片 （BGR）
            b, g, r = cv2.split(frame)  # 分离BGR三个通道
            merged = cv2.merge([b, g, r])  # 合并三个通道

            # 原始图像
            cv2.imshow('image', frame)
            # 单通道的灰度图
            cv2.imshow("Blue 1", b)
            # 单通道的通道合并
            zeros = np.zeros(frame.shape[:2], dtype="uint8")
            merged_r = cv2.merge([b, zeros, zeros])
            cv2.imshow("merged_b", merged_b)

            cv2.waitKey(1)  # 括号内为0时 只取第一张图 ； 为1时实时显示

    return color





