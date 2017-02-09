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
  time.sleep(0.00001)                    #Pulse ping for 10uSec
  GPIO.output(trig, False)               #Turn off ping trigger
  
  while GPIO.input(echo)==0:             #Echo low, start listen time
    pulse_begin = time.time()            #Save time of last low pulse
  while GPIO.input(echo)==1:             #Wait/test for Echo high. End listen time
     pulse_end = time.time()             #Save time of last high pulse
  print('Reading Finished')
  pulse_width = pulse_end - pulse_begin  #Calculate time for round trip of pulse to object and back
  
  #Sea level speed of sound=34300 cm/sec. 
  #Divide pulse_width by 2 to get time of one-way (1/2 round) trip.
  dist = pulse_width * 34300 / 2      #Pulse width (sec)/2*Speed of sound (cm/sec) is cm distance
  dist = round(dist - offset, 1)         #Calibrate result and round to 1/10th of cm
  if dist > 2 and dist < 400:            #Sensor range is 2cm to 400cm
    print('Distance = ',dist,' cm')      #Print calibrated distance measurement
  else:
    print('Out of 2cm to 4meter Range!') #If out of range print error message
 #End of indented for x in range loop
GPIO.cleanup()                           #Reset GPIO ports
print('Done')                            #Print "Done" to show program ended normally
