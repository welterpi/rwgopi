import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 13
ECHO = 26

print "Distance Measurement in Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for Sensor"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
