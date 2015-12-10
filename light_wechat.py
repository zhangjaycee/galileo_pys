#! /usr/bin/env python
import sys 
import urllib2
import time
import pyupm_grove as grove

led = grove.GroveLed(3)
light = grove.GroveLight(2)

print "[start....]"
time.sleep(20)
while True:
	light_value = light.raw_value()
	
	data = '''<xml>
	 <light><![CDATA[%s]]></light>
	</xml>''' % light_value
	
	cookies = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookies)
	
	request = urllib2.Request(
	        url = r'http://galileo.xdjc.date/?signature=1ce507b0abfa4d231b538988c01127c9e03a02ad&timestamp=1408377801&nonce=959202980',
	        headers = {'Content-Type' : 'text/xml'},
	        data = data)
	
	state = int(opener.open(request).read())
	if state == 2:
		if light_value <= 300:
        	        led.on()
        	else:
        	        led.off()
	elif state == 0:
		led.off()
	elif state == 1:
		led.on()
        time.sleep(1)

