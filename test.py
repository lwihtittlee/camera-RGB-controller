import cv2

clicked = False #鼠标是否被按下

def onMouse(event,x,y,flags,param):
    '''图像坐标系的坐标（不是窗口坐标系）
    flags:鼠标回调
    define:鼠标操作响应函数

    event:鼠标回调事件参数
    x,y:鼠标指针在的标志参数
    param:param是用户定义的传递到setMouseCallback函数调用的参数
    '''
    #声明clicked为全局变量
    global clicked
    '''    func:每次在图像上单击鼠标左键再抬起的过程，setMouseCallback()都会分3次调用鼠标响应函数，并且响应顺序是：

    1.左键单击按下；

    2.左键单击抬起； 

    3.鼠标指针位置移动（即使原地单击，鼠标位置并没有移动）；
    '''
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
        print("cliked")

#公共接口，无论是从摄像头还是视频文件读入，都调用此函数**
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('mywindow')
#鼠标响应事件函数，调用鼠标操作响应函数**
cv2.setMouseCallback('mywindow',onMouse)

print('showing camera feed. cliked window or press any ket to stop')
#获取当前帧以及读取状态**
success,frame = cameraCapture.read()
#当成功获取当前帧且鼠标未被按下时**
while success and not clicked:
    cv2.imshow('mywindow',frame)
    #每1ms刷新一次
    cv2.waitKey(1)
    success,frame = cameraCapture.read()

#销毁窗口并释放**
cv2.destroyWindow('mywindow')
cameraCapture.release()
