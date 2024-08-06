# -*- coding: UTF-8 -*-
 
import cv2

import mediapipe as mp
import numpy as np
import time



hand_nums=2 # 表示能支持的车数量

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2) # 参数1图片or视频，参数2手数量，参数3复杂度，参数4置信度，参数跟踪置信度
mpDraw = mp.solutions.drawing_utils # 库自带的画线画点方法
handLmsStyle = mpDraw.DrawingSpec(color=(0,0,255),thickness=5) # BGR 点
handConStyle = mpDraw.DrawingSpec(color=(0,255,0),thickness=10) # BGR  线

cTime=0
pTime=0

wCam ,hCam = 1280,780

cap.set(3,wCam)# 设置摄像头分辨率
cap.set(4,hCam)

w_interval = [0.1, 0.2, 0.3, 0.4,0.5,0.6,0.7,0.8,0.9,1] # TODO 数量需等于
h_interval=[0.1,0.3,0.5]

nums_w=len(w_interval)
nums_h=len(h_interval)
leds=[nums_w,nums_h] 




while True:
    ret, img = cap.read()
    h, w, c = img.shape  # 图片的高度 ，宽度

    if ret:
        img=cv2.flip(img,2)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        # print(result.multi_hand_landmarks) # 手的标记点
        # b_bool=[[True]*len(w_interval)]*len(h_interval)
        b_bool=np.array([[True]*len(w_interval)]*len(h_interval))
        
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                
                for i,lm in enumerate(handLms.landmark): # 遍历所有手的所有坐标
                    
                    # for lm in handLMs.landmark:
                    x, y = (lm.x ), (lm.y )
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
 
                a=[x_min,x_max]
                result = np.digitize(a, w_interval)
                
                a=[y_min,y_max]
                result_h=np.digitize(a, h_interval)
                # print(result_h)
                # for i in result_h:
                #     if i 
                c=np.array([[False]*(result_h[1]-result_h[0])]).T
                # b=np.array([[1]*(sets2[1]-sets2[0])]).T
                # print(c)
                
                b_bool[nums_h-result_h[1]:nums_h-result_h[0],result[0]:result[1]]=c
                # print(b_bool)

                
                # c=np.array([[1,1,1]]).T
                # b_bool[result_h[0]:result_h[1],[1]]=c
                
                # d=np.array([False]*(result[1]-result[0]))
                # b_bool[[1],result[0]:result[1]]=d
        for j in range(nums_h):
            h_off=int(h*0.1*j)
            for i in range(nums_w):
                r=20
                if b_bool[j][i]:
                    cv2.circle(img, (int(i*(w/nums_w))+int((w/nums_w)/2), h-r-10-h_off), r, (0, 0, 255), -1) 
                else:
                    cv2.circle(img, (int(i*(w/nums_w))+int((w/nums_w)/2), h-r-10-h_off), r, (0, 0, 255), 1)     

        cv2.imshow('img',img)

    key = cv2.waitKey(1)
    if key != -1:
        break

cap.release()

