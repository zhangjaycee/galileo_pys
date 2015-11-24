import time
import pyupm_grove as grove

led = grove.GroveLed(3)
light = grove.GroveLight(2)

print "led name:",led.name()

for i in range (0,3):
    led.on()
    time.sleep(2)
    print light.name() + "[ON]" + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(2)
    print light.name() + "[ON]" + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(2)
    led.off()
    time.sleep(2)                                     
    print light.name() + "[OFF]" + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(2)
    print light.name() + "[OFF]" + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(2)            
# Delete the Grove LED object
del led
