import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(31,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(35,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(37,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(36,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(40,GPIO.OUT,initial=GPIO.LOW)
GPIO.setwarnings(False)

pins=[29,31,33,35,37,36,38,40]
while True:
	c=8
	for i in pins[::-1]:
		for j in pins[:c:]:
			GPIO.output(j,GPIO.HIGH)
			sleep(2)
			GPIO.output(j,GPIO.LOW)
			sleep(1)
		GPIO.output(i,GPIO.HIGH)
		sleep(1)
		GPIO.output(i,GPIO.LOW)
		c-=1
