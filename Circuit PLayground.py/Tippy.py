from adafruit_circuitplayground import cp


while True:
    if cp.acceleration.x > 3:
        for i in range(1,4):
            cp.pixels[i] = (5,0,0)
    elif cp.acceleration.x < -3:
        for i in range(6,9):
            cp.pixels[i] =(0,5,0)
    else:
            cp.pixels.fill((0,0,0))