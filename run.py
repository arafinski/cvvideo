import time
from button import *
from oledVideo import *
from hdmiVideo import *
from video import *

switch = getSwitch()
previewButton = getGreen()
nextButton = getBlue()
lastButton = getBlack()

loop = False


def switchTrue():
    global loop
    if loop == False:
        loop = True



def checkInput():
    global loop
    switch = getSwitch()
    previewButton = getGreen()
    nextButton = getBlack()

    if previewButton == False:
        switchTrue()

        # print('switch false')
        # time.sleep(0.2)
    else:
        loop = False

oLEDActive = False
allowedToTriggerNextVideo = False

def checkLoopStatus():
    global loop
    global oLEDActive
    global allowedToTriggerNextVideo
    getKnob(4)
    getAdc(0)
    if loop == True:
        if oLEDActive == False:
            activeOLEDmain()
            oLEDActive = True
            allowedToTriggerNextVideo = True
    else:
        oLEDActive = False
        if allowedToTriggerNextVideo == True:
            playVideo(getLastVideo())
            allowedToTriggerNextVideo = False




while True:
     # button()
     checkInput()
     checkLoopStatus()


# while loop == True:
#     print('switching on')
