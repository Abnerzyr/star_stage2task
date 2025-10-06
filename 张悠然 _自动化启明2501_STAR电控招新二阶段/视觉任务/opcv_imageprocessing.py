import cv2 as cv
import numpy as np
img=cv.imread("testhuohuo.jpg")

hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)#转换为HSV色彩空间

#设定绿色范围
lower_green = np.array([40, 30, 30])   
upper_green = np.array([90, 255, 255]) 

#创建掩膜
green_mask = cv.inRange(hsv_image, lower_green, upper_green)
k=np.ones((5,5),np.uint8)#定义核大小

# #进行开运算，去除外部细节
# opened_mask = cv.morphologyEx(green_mask, cv.MORPH_OPEN, k)

# #进行闭运算，填补内部空洞
# closed_mask = cv.morphologyEx(opened_mask, cv.MORPH_CLOSE, k)

# final_mask=closed_mask
##测试发现去噪声处理偏差略大，直接用原掩膜过滤过小色块处理

#寻找轮廓
contours, hierarchy = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
#计算重心并输出
for cnt in contours:
    M = cv.moments(cnt)
    if M["m00"] != 0 and M["m00"] > 20:  # 防止除0错误并过滤过小色块
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(f"重心坐标：(", cX, ",", cY, ")")
#可视化调试处理
        cv.circle(img, (cX, cY), 7, (0, 0, 255), -1)
cv.imshow("orimask",green_mask)
cv.imshow("image",img)
# cv.imshow("mask",final_mask)
cv.waitKey(0)
cv.destroyAllWindows()

