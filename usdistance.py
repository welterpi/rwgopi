#Python 3 program for HC-SR04 Ultrasonic Sensor using polling
#Output (ping) on pin 11, input (listen) on pin 33, pin 6 GND
#5Vcc pin must go to RPi pin 2, trig pin to RPi pin 11
#Echo MUST go through voltage divider circuit !!!!
#Echo -> 4.7k Ohm resistor -> RPi pin 13 + 10k Ohm -> RPi & SR0-
import RPi.GPIO as GPIO                  #Import GPOI Library
import time                              #Import time Library
GPIO.setmode(GPIO.BOARD)                 #Use GPIO pin location numbering
trig = 11                                #Set trigger pin
echo = 13                                #Set echo pin
offset = round (0.6, 2)                  #Offset to calibrate distance to your zero location
GPIO.setup(trig,GPIO.OUT)                #Set trigger as output
GPIO.setup(echo,GPIO.IN)                 #Set echo as input

for x in range(0, 50):                   #Loop x times
  print('Setting Up')                    #Show program has started at top of loop
  GPIO.output(trig, False)               #Turn off ping trigger
  time.sleep(2)                          #Delay so sensor settles before ping
  
  print('Ping 8x40kHz pulses (trigger)')
  GPIO.output(trig, True)                #Turn on ping trigger
 
