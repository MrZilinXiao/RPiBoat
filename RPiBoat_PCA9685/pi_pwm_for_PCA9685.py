#!/usr/bin/python
# -*- encoding: UTF-8 -*-
import time
from smbus import SMBus
from PCA9685 import PWM
#import RPi.GPIO as GPIO
#import atexit
#atexit.register(GPIO.cleanup)

fPWM = 50
i2c_address = 0x40
channel_s1 = 0
channel_m1 = 7


if __name__ == "__main__":
    servo = 50
class PiPWM():
    def __init__(self):
        global pwm
        self.bus = SMBus(1)
        pwm = PWM(self.bus, i2c_address)
        pwm.setFreq(fPWM)
        self.isM1start = False
        self.isS1start = True
        time.sleep(0.5)
        self.set_dc_for_s1(7.2)
        #time.sleep(0.5)
        #self.set_dc_for_m1(9.5)
        #time.sleep(3)
        self.set_dc_for_m1(5)
        #time.sleep(3)
        print "Calibration Complete!"
    def stop(self):
        self.set_dc_for_s1(0)
        self.set_dc_for_m1(0)
    def emergency_stop(self):
        self.set_dc_for_m1(5)
        print "EMERGENCY STOP OK!"
    def set_dc_for_s1(self, dc):
        pwm.setDuty(channel_s1,dc)
    def set_dc_for_m1(self,dc):
        pwm.setDuty(channel_m1,dc)
        #self.m1.ChangeDutyCycle(dc)
    def motor_set(self, percent):
        if 0 <= percent <= 100:
            if 0<= percent < 50:
                speed_percent = 4 + 1 * (percent / 50)
            else:
                speed_percent = 5 + 4.5 * ((percent-50)/50)
            print(speed_percent)
            self.set_dc_for_m1(speed_percent)
            print("motor_set: " + str(speed_percent))
            return "ok"
        else:
            return "invaild percent"
    def servo_set(self, percent):
        if 0 <= percent <= 100:
            if 0<= percent <=50:
                percent = 40 + 10 * (float(percent)/50)
            else:
                percent = 50 + 12 * (float(percent-50)/50)
            speed_percent = 3.2 + 8 * (percent / 100)
            self.set_dc_for_s1(speed_percent)
            # time.sleep(0.02)
            print("servo1_set: " + str(speed_percent))
            # self.s1.ChangeDutyCycle(0)
            # time.sleep(0.01)
            return "ok"
        else:
            return "invalid percent"

if __name__ == "__main__":
    pwm1 = PiPWM()
    try:
        while True:
        #    i = float(input("servo?(0-100 percentages)"))
        #    pwm1.servo_set(i)
        #    print("------" + str(i))
            j = float(input("servo?(0-100%)"))
            pwm1.servo_set(j)
            print("------" + str(j))
    except KeyboardInterrupt:
        pass
    pwm1.stop()

