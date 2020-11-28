from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import time
import board
import neopixel
 
pixel_pin = board.D18
 
num_pixels = 100
 
ORDER = "BRG"

enabled = True
color = 255

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = 1.0, auto_write = False, pixel_order = ORDER)
 
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

while True:
    if enabled == True:
        pixels.fill((255, 255, 255))
    
    else:
        pixels.fill((0, 0, 0))
        
    pixels.show()
    time.sleep(1)
 
try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")