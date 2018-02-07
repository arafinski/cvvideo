import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    green = GPIO.input(16)
    black = GPIO.input(20)
    blue = GPIO.input(21)
    switch = GPIO.input(26)
    if green == False:
        print('green Pressed')
        time.sleep(0.2)
    elif black == False:
        print('black Pressed')
        time.sleep(0.2)
    elif blue == False:
        print('blue Pressed')
        time.sleep(0.2)
    elif switch == False:
        print('switch false')
        time.sleep(0.2)
    elif switch == True:
        print('switch true')
        time.sleep(0.2)
