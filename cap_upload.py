#!/usr/bin/env python
import sys
import os 
import time
import cv2

print "starting camera..."
cam = cv2.VideoCapture(0)
count = 0
while True:
	ret, frame = cam.read()
	if ret:
	        cv2.imwrite('/home/root/galileo.jpg',frame)
        	os.system("scp /home/root/galileo.jpg root@xdjc.date:/root/wechat_galileo/")
		count += 1
		print "[upload ok],count =", count
	time.sleep(15)
