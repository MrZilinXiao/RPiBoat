import time
import RPi.GPIO as GPIO
import atexit
atexit.register(GPIO.cleanup)
motor_pin=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin,GPIO.OUT)

motor = GPIO.PWM(motor_pin,400)

def changePower(power):
    motor.ChangeDutyCycle(power)
    print "Power:"+str(power)+" "+"dc:"+str(power)

motor.start(0)
#changePower(90)

time.sleep(3)

print "High finished!"

#changePower(30)

time.sleep(6)

print "Low finished!"

for power in range(30,90,1):
    changePower(power)
    time.sleep(0.5)
motor.stop()
