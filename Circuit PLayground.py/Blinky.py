from adafruit_circuitplayground import cp


cp.pixels.brightness = (0.4)


import time


while True:
    cp.pixels.fill((0, 255, 0))
    time.sleep(.367)
    cp.pixels.fill((0,0,0,))
    time.sleep(.367)