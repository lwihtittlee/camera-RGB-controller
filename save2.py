import cv2

cap = cv2.VideoCapture(0)   # 从视频流循环帧
i = 0
while (1):
    ret, frame = cap.read()
    # ret 为True 或者False,代表有没有读取到图片
    # frame表示截取到一帧的图片
    k = cv2.waitKey(1)    # keep waiting
    if k == ord('b'):
        break
    elif k == ord('s'):
        cv2.imwrite('C:/Users/shalf/Desktop/lc-video/save/' + str(i) + '.jpg', frame)
        i += 1
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()
