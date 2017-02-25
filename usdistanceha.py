#Python 3 program for HC-SR04 Ultrasonic Sensor using polling
#Better accuracy with multiple readings - high & low discarded
#Output (ping) on pin 11, input (listen) on pin 33, pin 6 GND
#5Vcc pin must go to RPi pin 2, trig pin to RPi pin 11
#Echo MUST go through voltage divider circuit !!!!
#Echo -> 4.7k Ohm resistor -> RPi pin 13 + 10k Ohm -> RPi & SR0-

def usdistance(trig,echo,samp):
  discard = int(samp * 0.2)                #Discard % of high and low readings
  GPIO.setup(trig,GPIO.OUT)                #Set trigger as output
  GPIO.setup(echo,GPIO.IN)                 #Set echo as input
  summedtimes = 0                          #Reset (zero) sum of median times
  pulse_begin = 0; pulse_end = 0           #Reset (zero) variables
  avgdist = 0; sumdist = 0                 #Reset (zero) variables
  timelist = []                            #Store times in a list variable
  
  for x in range(0, samp):                 #Loop for each sample x times
    #  print('Setting Up')                    #Show program has started at top of loop
    GPIO.output(trig, False)               #Turn off ping trigger
    time.sleep(0.010)                       #Delay so sensor settles before ping
  
    #  print('Ping 8x40kHz pulses (trigger)')
    GPIO.output(trig, True)                #Turn on ping trigger
    time.sleep(0.00001)                    #Pulse ping for 10uSec
    GPIO.output(trig, False)               #Turn off ping trigger
  
    while GPIO.input(echo)==0:             #Echo low, start listen time
      pulse_begin = time.time()            #Save time of last low pulse
    while GPIO.input(echo)==1:             #Wait/test for Echo high. End listen time
       pulse_end = time.time()             #Save time of last high pulse
    print('Reading Finished')
    pulse_width = pulse_end - pulse_begin  #Calculate time for round trip of pulse to objectand back
    timelist.append(pulse_width)           #Put each round trip time reading at the end of the list of values
    print('Reading ' + str(x+1) + '/' + str(samp), str(pulse_width))
    #End of indented for x in range loop

  for y in range(discard, (samp - discard)):  #Ignore the highest and lowest values in the list
    summedtimes += timelist[y]             #Add up the median values of the list
    #End of indented for y in range loop    

    #Sea level speed of sound=34300 cm/sec  . 
    #Divide pulse_width by 2 to get time of   one-way (1/2 round) trip.
  sumdist = summedtimes * 34300 / 2      #  Pulse width (sec)/2*Speed of sound (cm/sec) is cm distance
  avgdist = round((sumdist / (samp - discard * 2)) - offset, 1)         #Calibrate result and round to 1/10th of cm
  if avgdist > 2 and avgdist < 400:                #Sensor range is 2cm to 400cm
    print('Distance = ',avgdist,' cm')      #Print calibrated distance measurement
  else:
      print(avgdist,' Out of 2cm to 4meter Range!') #If out of range print error mess  age
  return avgdist


import RPi.GPIO as GPIO                  #Import GPOI Library
import time                              #Import time Library

GPIO.setmode(GPIO.BCM)                   #Use GPIO BCM I/O numbering
trig = 13                                #Set trigger pin
echo = 26                                #Set echo pin
samp = 50                                #Number of samples per reading
offset = round (0.6, 2)                  #Offset to calibrate distance to your zero location

#usdistance(trig,echo,samp)
print('Distance = ',usdistance(trig,echo,samp),' cm')      #Print calibrated distance measurement

GPIO.cleanup()                           #Reset GPIO ports   
print('Done')                            #Print "Done" to show program ended norma  ll       
