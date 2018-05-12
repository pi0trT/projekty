import RPi.GPIO as GPIO
import time
import os
import datetime
from time import gmtime, strftime
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(4, GPIO.IN)
zmienna1="fswebcam --fps 10 -r 1280x720 -s 20 -d /dev/video0 /home/pi/webcam/"
zmienna2=".jpg"
while True:
    if (GPIO.input(4)==True):
        today = strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        today2 = str(today)
        polecenie_systemowe=zmienna1+today2+zmienna2
        print("wykryto ruch")
        print today
        os.system(polecenie_systemowe)
        time.sleep(2)