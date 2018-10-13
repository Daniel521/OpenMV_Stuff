#   Blinking LED
#   10/12/2018
#   Daniel Verdugo
#   Riad Soliven
#   Peter

import pyb
import utime

red_led = pyb.LED(1)
green_led = pyb.LED(2)
blue_led = pyb.LED(3)
ir_led = pyb.LED(4)

red_led.off()
green_led.off()
blue_led.off()
ir_led.off()

while True:
    utime.sleep_ms(500)
    red_led.toggle()
    green_led.toggle()
    blue_led.toggle()
