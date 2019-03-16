#!/usr/bin/python2
# -*- encoding: UTF-8 -*-

from smbus import SMBus
from PCA9685 import PWM #从PCA9685引入PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) 根据连接舵机的接口设置I2C地址
channel = 0 # 舵机连接的控制板接口

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(percent):
    duty = 3.2 + 8 * (float(percent) / 100)
    pwm.setDuty(channel, duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) 
print "starting"
setup()
for direction in range(0, 180, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
print "done"
