import os
import cv2
import sendweibo


print "hello!"
cam = cv2.VideoCapture(0)

ret, frame = cam.read()
if ret:
	cv2.imwrite('frame.png',frame)
	
	sendweibo.post_pic(s, addr)
