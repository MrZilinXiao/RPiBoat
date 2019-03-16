import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

servopin=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin,GPIO.OUT,initial=False)
p=GPIO.PWM(servopin,50)
p.start(0)
time.sleep(0.1)
while(True):
	i = float(raw_input("degree?"))
	p.ChangeDutyCycle(2.5 + 10 * i / 180)  
	time.sleep(0.02)
	p.ChangeDutyCycle(0)  
	time.sleep(0.2)