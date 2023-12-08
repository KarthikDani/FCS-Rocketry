# GPIO mode

from hx711_gpio import HX711
from machine import Pin
from utime import sleep

pin_OUT = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(18, Pin.OUT)

hx711 = HX711(pin_SCK, pin_OUT)

# First tare the initial weight when bottle is not put
#hx711.tare()

# Customised caliberation factor done with known weight
caliberation_factor = 1 / 0.00235 # for grams
hx711.set_scale(caliberation_factor)

while True:
    weight = hx711.get_units()
    print("Weight:", weight)