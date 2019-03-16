#!/usr/bin/python
# -*- encoding: UTF-8 -*-
"""
Use PWM contoll ESC motor and Servo
Brushless Motor 1 ESC connected to GPIO 12, Servo 1 connect to GPIO 18

"""

import time
import RPi.GPIO as GPIO
import atexit
atexit.register(GPIO.cleanup)

if __name__ == "__main__":
    servo = 50


class PiPWM():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)

        self.m1 = GPIO.PWM(12, 400)
        self.s1 = GPIO.PWM(18, 50)

        self.m1.start(0)
        self.s1.start(0)
        self.isM1start = False
        self.isS1start = True

        time.sleep(0.5)
        #self.m1.ChangeDutyCycle(0)
        self.s1.ChangeDutyCycle(7.2) # 启动时舵机置中
        time.sleep(0.5)
        # 启动校准油门行程
        self.m1.ChangeDutyCycle(90) # 油门上界
        time.sleep(3)
        self.m1.ChangeDutyCycle(30) # 油门下界
        time.sleep(3)
        print "油门校准完成！"

    def stop(self):
        self.m1.stop()
        self.s1.stop()
        GPIO.cleanup()

    def motor_set(self, percent):
        if 0 <= percent <= 100:
            if not self.isM1start:
                # self.m1 = GPIO.PWM(12, 50)
                self.m1.start(0)
                time.sleep(0.02)
                self.isM1start = True
            speed_percent = 30 + 60 * (percent / 100)
            print(speed_percent)
            self.m1.ChangeDutyCycle(speed_percent)
            print("motor_set: " + str(speed_percent))

            time.sleep(0.02)
            return "ok"
        else:
            return "invalid percent"

    def servo1_set(self, percent):
        if 0 <= percent <= 100:
            if not self.isS1start:
                self.s1 = GPIO.PWM(18, 50)
                self.s1.start(0)
                time.sleep(0.05)
                self.isS1start = True
            speed_percent = 3.2 + 8 * (percent / 100)
            self.s1.ChangeDutyCycle(speed_percent)
            # time.sleep(0.02)
            print("servo1_set: " + str(speed_percent))
            # self.s1.ChangeDutyCycle(0)
            time.sleep(0.05)
            return "ok"
        else:
            return "invalid percent"


if __name__ == "__main__":
    pwm1 = PiPWM()
    try:
        while True:
            i = float(input("servo?(0-100 percentages)"))
            pwm1.servo1_set(i)
            print("------" + str(i))
    except KeyboardInterrupt:
        pass
    pwm1.stop()
