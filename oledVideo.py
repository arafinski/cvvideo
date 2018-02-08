#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Display a video clip.

Make sure to install the av system packages:

  $ sudo apt-get install -y libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libavresample-dev libavfilter-dev

And the pyav package (might take a while):

  $ sudo -H pip install av
"""

import sys
import os
import os.path
from demo_opts import get_device
import RPi.GPIO as GPIO
from button import *
from run import *

import math
import datetime
from luma.core.render import canvas
from PIL import ImageFont
#
#
# GPIO.setmode(GPIO.BCM)
#
# GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)



import PIL

import random


try:
    import av
except ImportError:
    print("The pyav library could not be found. Install it using 'sudo -H pip install av'.")
    sys.exit()

device = get_device()

lastVideo = ""

def getLastVideo():
    return lastVideo

def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    return ImageFont.truetype(font_path, size)



def drawToOLED(value):
    if (isinstance(value, basestring) == False):
        value = "%.2f" % value
    # DS-DIGI
    font = make_font("miscfs_.ttf", device.height - 8)
    # font = make_font("fontawesome-webfont.ttf", device.height - 10)
    with canvas(device, dither=True) as draw:
    		# draw.rectangle((10, 10, 30, 30), outline="white", fill="red")
    		#draw.rectangle(device.bounding_box, outline="white", fill="black")
            # draw.textsize(str(value))
    		draw.text((13, 3), str(value), fill="white", font=font)

def runMainOLED():
    global mainOLEDRunning

    with canvas(device, dither=True) as draw:
    		draw.rectangle((10, 10, 30, 30), outline="white", fill="red")
    		#draw.rectangle(device.bounding_box, outline="white", fill="black")

    		draw.text((3, 3), "12345678901234567890", fill="white")
    # mainOLEDRunning ==


def activeOLEDmain():
    global lastVideo

    video_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
        '/home/pi/cvvideo/videos', random.choice(os.listdir("/home/pi/cvvideo/videos"))))
    print('Loading {}...'.format(video_path))
    lastVideo = video_path

    clip = av.open(video_path)


    for frame in clip.decode(video=0):
        if getGreen() == False:
        # input_state = GPIO.input(16)
        # if input_state == False:
            print('{} ------'.format(frame.index))
            nextButton = getBlack()
            if nextButton == False:
                device.clear()
                activeOLEDmain()
                return


            img = frame.to_image()
            if img.width != device.width or img.height != device.height:
                # resize video to fit device
                size = device.width, device.height
                img = img.resize(size, PIL.Image.ANTIALIAS)

            device.display(img.convert(device.mode))

        else:
            device.clear()
            return

    device.clear()


#
# if __name__ == "__main__":
#     try:
#         device = get_device()
#         while True:
#             input_state = GPIO.input(16)
#             if input_state == False:
#                 #print('Button Pressed')
#                 main()
#             else:
#                 device.clear()
#
#     except KeyboardInterrupt:
#         pass
