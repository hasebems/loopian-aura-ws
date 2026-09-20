import neopixel
from machine import Pin
import time
pixels = neopixel.NeoPixel(Pin(26), 6, bpp=4)
RED   = (255, 0, 0, 0)
BLUE  = (0, 0, 255, 0)
GREEN = (0, 255, 0, 0)
WHITE = (0, 0, 0, 255)
OFF   = (0, 0, 0, 0)
cnt = 0
while True:
    pixels[(0 + cnt)%6] = RED
    pixels[(1 + cnt)%6] = BLUE
    pixels[(2 + cnt)%6] = GREEN
    pixels[(3 + cnt)%6] = RED
    pixels[(4 + cnt)%6] = BLUE
    pixels[(5 + cnt)%6] = GREEN
    pixels.write()
    time.sleep(1)
    cnt += 1