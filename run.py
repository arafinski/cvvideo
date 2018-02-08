import time
from button import *
from hdmiVideo import *
from oledVideo import *
from video import *

switch = getSwitch()
previewButton = getGreen()
nextButton = getBlue()
lastButton = getBlack()

oledPreviewTriggered = False


def switchTrue():
    global oledPreviewTriggered
    if oledPreviewTriggered == False:
        oledPreviewTriggered = True



def checkInput():
    global oledPreviewTriggered
    switch = getSwitch()
    previewButton = getGreen()
    nextButton = getBlack()

    if previewButton == False:
        switchTrue()

        # print('switch false')
        # time.sleep(0.2)
    else:
        oledPreviewTriggered = False

oLEDActive = False
allowedToTriggerNextVideo = False
mainOLEDRunning = False
oledMainActive = False

def checkoledPreviewTriggeredStatus():
    global oledPreviewTriggered
    global oLEDActive
    global allowedToTriggerNextVideo
    global mainOLEDRunning
    global oledMainActive
    getKnob(4)
    getAdc(0)
    if oledPreviewTriggered == True:
        if oLEDActive == False:
            mainOLEDRunning = False
            activeOLEDmain()
            oLEDActive = True
            allowedToTriggerNextVideo = True
            oledMainActive = False
    else:
        oLEDActive = False
        if oledMainActive == False:
            mainOLEDRunning = True
            print('_______running MAINOLED')
            runMainOLED()
            oledMainActive = True

        if allowedToTriggerNextVideo == True:
            playVideo(getLastVideo())
            allowedToTriggerNextVideo = False


if __name__ == "__main__":
    while True:
        try:
            checkInput()
            checkoledPreviewTriggeredStatus()
        except (KeyboardInterrupt, SystemExit):
            killVideo()
            raise
