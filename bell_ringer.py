#!/usr/bin/python
#### RING THE BELL!!!

## Run this on a cron job every 5-10 minutes


#### initialize the stuff
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

#### Logging
import logging
logging.basicConfig(filename='/fruit/bell/example.log',level=logging.INFO,format='%(asctime)s %(message)s')

logging.info('Start Bell Ringer')

#### Functions
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

#### Variables
mh = Adafruit_MotorHAT(addr=0x61)
atexit.register(turnOffMotors)
myMotor = mh.getMotor(3)

#### check the API

logging.info('Checking the API')



#### If ring, ring the bell
ring_time = .25
i=255
x=True
ring_count = 5
while (x):
	print "RINGGGGG! "
	logging.info('Ringing the bell for SOME DEAL!!')
	myMotor.run(Adafruit_MotorHAT.FORWARD)
	myMotor.setSpeed(i)
	time.sleep(ring_time)
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(ring_time*2)
	ring_count -= 1
	if ring_count < 1:
		x=False



#### Shutdown
