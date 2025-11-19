from adafruit_circuitplayground import cp



import time

while True:
    cp.pixels.fill((255, 0, 0))
    time.sleep(0.500)
    cp.play_tone(500, 0.25)
    cp.pixels.fill((0, 0, 255))
    time.sleep(0.500)
    cp.play_tone(900, 0.25)