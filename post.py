#! /usr/bin/env python
import sys
import os 
import urllib2
import cv2

t = sys.argv[1]

data = '''<xml>
 <temprature><![CDATA[%s]]></temprature>
</xml>''' % t 
 
cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
 
request = urllib2.Request(
        url = r'http://galileo.xdjc.date/?signature=1ce507b0abfa4d231b538988c01127c9e03a02ad&timestamp=1408377801&nonce=959202980',
        headers = {'Content-Type' : 'text/xml'},
        data = data)
 
print opener.open(request).read()


print "starting camera..."
cam = cv2.VideoCapture(0)

ret, frame = cam.read()
if ret:
        cv2.imwrite('galileo.jpg',frame)
        os.system("scp /home/root/wechat/galileo.jpg root@xdjc.date:/root/wechat_galileo/")
