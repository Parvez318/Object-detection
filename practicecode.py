import cv2
import numpy as np

img_rgb = cv2.imread('streetss.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('streets1.jpg',0)
template2 = cv2.imread('streets2.jpg',0)
w, h = template1.shape[::-1]
w, h = template2.shape[::-1]
res1 = cv2.matchTemplate(img_gray,template1,cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
threshold1 = 0.9
threshold = 0.8
loc1 = np.where( res1 >= threshold1)
for pt in zip(*loc1[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
loc2 = np.where( res2 >= threshold)
for pt in zip(*loc2[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Detected',img_rgb)

