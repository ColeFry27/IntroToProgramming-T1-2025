from adafruit_circuitplayground import cp

import random
cp.pixels.brightness = 0.3

while True:
    shake_threshold = 15.0
    if abs(cp.acceleration.x) > shake_threshold or abs(cp.acceleration.y) > shake_threshold or abs(cp.acceleration.z) > shake_threshold:
        for i in range(0,10):
            r = random.randint(0, 255)
            x = random.randint(0, 255)
            c = random.randint(0,255)
            cp.pixels[i] = (r, x, c)

