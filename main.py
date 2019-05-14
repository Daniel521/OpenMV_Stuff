# AprilTag Detection
# 

import sensor, image, time, math
from pyb import UART
from pyb import LED
import utime

red_led = LED(1)
red_led.on()
green_led = LED(2)

uart = UART(3, 9600, timeout_char = 1000)
uart.init(9600, bits=8, parity=None, stop=1, timeout_char=1000)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # we run out of memory if the resolution is much bigger...
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()

tag_families = 0
tag_families |= image.TAG16H5
#tag_families |= image.TAG25H7
#tag_families |= image.TAG25H9
#tag_families |= image.TAG36H10
#tag_families |= image.TAG36H11
#tag_families |= image.ARTOOLKIT

def family_name(tag):
	if(tag.family() == image.TAG16H5):
		return "TAG16H5"
	if(tag.family() == image.TAG25H7):
		return "TAG25H7"
	if(tag.family() == image.TAG25H9):
		return "TAG25H9"
	if(tag.family() == image.TAG36H10):
		return "TAG36H10"
	if(tag.family() == image.TAG36H11):
		return "TAG36H11"
	if(tag.family() == image.ARTOOLKIT):
		return "ARTOOLKIT"


while(True):
	clock.tick()
	img = sensor.snapshot()
	for tag in img.find_apriltags(families=tag_families):
		img.draw_rectangle(tag.rect(), color = (255, 0, 0))
		img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
		print_args = (family_name(tag), tag.id(), (180 * tag.x_rotation()) / math.pi)
		uart.write("%dt" % tag.id())
		#print("%dt" % tag.id())
		if tag.cx() < (img.width() / 3):
			uart.write("ro")
			#print("ro")
		elif tag.cx() > (img.width() * 2 / 3):
			uart.write("lo")
			#print("lo")
		else:
			uart.write("so")
			#print("so")
		green_led.on()
		utime.sleep_ms(200)
		green_led.off()
	#utime.sleep_ms(50)



