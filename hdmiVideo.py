import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import time
import random
import datetime

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep


import RPi.GPIO as GPIO




# --no-osd
# , '--loop'
#         dbus_name='org.mpris.MediaPlayer2.omxplayer1')

foo = ["/home/pi/cvvideo/videos/1.mp4", "/home/pi/cvvideo/videos/2.mp4", "/home/pi/cvvideo/videos/3.mp4", "/home/pi/cvvideo/videos/4.mp4", "/home/pi/cvvideo/videos/5.mp4", "/home/pi/cvvideo/videos/6.mp4", "/home/pi/cvvideo/videos/7.mp4", "/home/pi/cvvideo/videos/8.mp4", "/home/pi/cvvideo/videos/9.mp4", "/home/pi/cvvideo/videos/10.mp4", "/home/pi/cvvideo/videos/11.mp4", "/home/pi/cvvideo/videos/12.mp4", "/home/pi/cvvideo/videos/13.mp4", "/home/pi/cvvideo/videos/14.mp4", "/home/pi/cvvideo/videos/15.mp4", "/home/pi/cvvideo/videos/16.mp4", "/home/pi/cvvideo/videos/17.mp4", "/home/pi/cvvideo/videos/18.mp4", "/home/pi/cvvideo/videos/19.mp4", "/home/pi/cvvideo/videos/20.mp4", "/home/pi/cvvideo/videos/21.mp4", "/home/pi/cvvideo/videos/22.mp4", "/home/pi/cvvideo/videos/23.mp4", "/home/pi/cvvideo/videos/24.mp4", "/home/pi/cvvideo/videos/25.mp4", "/home/pi/cvvideo/videos/26.mp4", "/home/pi/cvvideo/videos/27.mp4", "/home/pi/cvvideo/videos/28.mp4", "/home/pi/cvvideo/videos/29.mp4", "/home/pi/cvvideo/videos/30.mp4", "/home/pi/cvvideo/videos/31.mp4", "/home/pi/cvvideo/videos/test.mp4"]

VIDEO_1_PATH = ("/home/pi/cvvideo/videos/test.mp4")
player = OMXPlayer(VIDEO_1_PATH, args=['--loop', '--no-osd'])
sleep(1)

# print(os.listdir("/home/pi/cvvideo/videos"))
#
player.play()

#! /usr/bin/env python
# python programa to comunicate with an MCP3008
# Import our SpiDe wrapper and our sleep function

import spidev
from time import sleep

# Establish SPI device on Bus 0,Device 0
spi = spidev.SpiDev()
spi.open(0,0)

try:
   lastvalue
except NameError:
    print('no lastvalue')
    lastvalue = -1

speed = 0

lastDatetime = datetime.datetime.now()
# GPIO.setmode(GPIO.BCM)
#
# GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def playVideo (videoPath):
    # player.next()
    # player.play()

    player.quit()

    # movie1 = random.choice(foo)
    player.load(videoPath)
    player.play()

knob = 1

def getKnob (channel) :
    global knob
    if ((channel>7)or(channel<0)):
        return -1
    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8+channel) << 4, 0])
    if r[1] > 1:
        if channel == 3:
            if r[2] == 255:
                print 'channel ', channel
        else:
            knobPercentage = float(r[2] - 30)/170
            if knobPercentage > 0:
                knob = float(r[2] - 30)/170
            # print(knob)

lastSpeed = 0

def getAdc (channel):
    global knob
    #check valid channel
    if ((channel>7)or(channel<0)):
        return -1


    # Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8+channel) << 4, 0])
   # print(r[1])
    #Filter data bits from retruned bits
    #adcOut = ((r[1]&3) << 8) + r[2]
    #percent = int(round(adcOut/10.24))
    #print("ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent))
    #print(r[1])
    #print out 0-1023 value and percentage


    global lastvalue
    global speed
    global lastSpeed
    global lastDatetime

    # green = GPIO.input(16)
    # if green == False:
    #     play()

    iTolerance = 50


    if lastvalue != r[2]:
        lastvalue = r[2]
        if lastvalue == 0:
            #how may bpm?
            #timedifference = datetime.datetime.now() - lastDatetime
            #bpm = 60 / test.total_seconds()
            #print(bpm)
            test = datetime.datetime.now() - lastDatetime
            difference = test.total_seconds()
            check = test.total_seconds() / 100
            if check < 0.01:
                bong = 1 / difference
                speed = bong / 2
                speed = speed * knob
                if (speed < (lastSpeed + (iTolerance *(lastSpeed/100)))) and (speed > (lastSpeed - (iTolerance *(lastSpeed/100)))):
                    print(speed)
                    print(lastSpeed)
                    player.set_rate(speed)
                lastSpeed = speed

            else:
                bong = difference / 100
                speed = difference * bong
                speed = speed * knob
                # print("speed!")
                # print(speed)
                player.set_rate(speed)
            # print(test.total_seconds())

            lastDatetime = datetime.datetime.now()





    else:
        #player.set_rate(0)
        lastvalue = 0


    #r[1] => 0-3
    #r[2] => 0-255

    # if r[1] > 2:
    #     movie1 = random.choice(foo)
    #     os.system('killall omxplayer.bin')
    #     print(chr(27) + "[2J")
    #     omxc = Popen(['omxplayer', '-b', '--loop', '--no-osd', movie1])
    #     sleep(1)
    #     print(chr(27) + "[2J")


##        #sound.play(loops = 0)
##        print(r[1])
##        print("ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent))
#    print("ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent))
  #  sleep(0.1)


# while True:
    # getAdc(0)
