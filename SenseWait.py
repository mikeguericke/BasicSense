#Set up the sense hat module in python
from sense_hat import SenseHat
import os
import time
sense = SenseHat()

#Set up Variables
delay = 0.5

#Set up the color pallet
R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
W = [255, 255, 255]
X = [0, 0, 0]
#O = [255, 165, 0]

#Set up the three scenes
dispOne = [
    W, W, W, R, R, W, W, W,
    W, W, R, R, R, R, W, W,
    W, R, R, R, R, R, R, W,
    R, R, R, R, R, R, R, R,
    W, W, W, R, R, W, W, W,
    W, W, W, R, R, W, W, W,
    W, W, W, R, R, W, W, W,
    W, W, W, R, R, W, W, W,
    ]

dispTwo = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]

dispThree = [
    B, B, B, B, R, R, R, R,
    B, B, B, B, R, R, R, R,
    B, B, B, B, W, W, W, W,
    B, B, B, B, W, W, W, W,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    ]

#Excute code
while True:
    sense.clear()
    sense.set_pixels(dispOne)
    sense.stick.wait_for_event(emptybuffer=True)
    time.sleep(delay)
    sense.clear()
    sense.set_pixels(dispTwo)
    sense.stick.wait_for_event(emptybuffer=True)
    time.sleep(delay)
    sense.clear()
    sense.set_pixels(dispThree)
    sense.stick.wait_for_event(emptybuffer=True)
    time.sleep(delay)
    sense.clear()
    sense.stick.wait_for_event(emptybuffer=True)
    time.sleep(delay)
