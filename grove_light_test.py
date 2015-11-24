import time
import pyupm_grove as grove

# Create the light sensor object using AIO pin 0
light = grove.GroveLight(2)

# Read the input and print both the raw value and a rough lux value,
# waiting one second between readings
while 1:
    print light.name() + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux";
    time.sleep(1)

# Delete the light sensor object
del light
