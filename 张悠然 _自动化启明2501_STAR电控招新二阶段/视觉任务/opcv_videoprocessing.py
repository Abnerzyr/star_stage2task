import cv2 as cv
import numpy as np


    # 读取视频
cap = cv.VideoCapture("testhuohuo.mp4")
    
    # 获取视频属性
fps = int(cap.get(cv.CAP_PROP_FPS))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))



# 定义绿色范围（HSV颜色空间）
lower_green = np.array([50, 50, 50])
upper_green = np.array([90, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # 转换到HSV颜色空间
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # 创建绿色掩膜
    mask = cv.inRange(hsv, lower_green, upper_green)
    
    
    # 输出处理后的结果（先将全部设置为黑色，再还原绿色部分）
    result_frame = np.zeros_like(frame) 
    result_frame[mask > 0] = frame[mask > 0]  
    
    # 显示结果
    cv.imshow('Green Only Video', result_frame)
    cv.imshow('Original Video', frame)
    key = cv.waitKey(1000//fps) 
    if key == 27:  # 按Esc键退出
        break

# 释放资源
cap.release()

cv.destroyAllWindows()

