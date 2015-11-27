#!/usr/bin/env python
import time
import pyupm_grove as grove

led = grove.GroveLed(3)
light = grove.GroveLight(2)

print "[start....]"

while True:
	light_value = light.raw_value()
	if light_value <= 300:
		led.on()
	else:
		led.off()
	time.sleep(1)
