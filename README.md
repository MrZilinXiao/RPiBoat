# RPiBoat

A project of Raspberry Pi for SCU EIE Boat Competition held by SCU Electronical Garden.

Script files in this repo will provide:
1. Communication with the App for PWM-based rudder and throttle control
2. Simple anti-fail strategy (via ping)

Development records are as follow in **Simplified Chinese**: [RPiBoat 船模大赛开发手记 基于Raspberry Pi 3B的船模控制系统开发流程](https://mrxiao.net/rpiboat.html "RPiBoat").

## Platform
- Raspberry Pi 3
- 2440 Brushless Motor
- ES08A Control Actuator
- 2200mAh 2S Battary
- Pi SCI Camera

## Configuration
1. Clone this resposity in your RPi.
2. Connect all necessary cables commented in source code files, which includes GPIO12 GPIO18 and 2 ground cables. (If you choose to use PCA9685 to generate PWM signals, take a look at my blog to see how to connect tables.)
3. Config your RPi Wi-Fi AP Mode and IP to make sure the access to your smartphones. You could visit [here](https://mrxiao.net/RPi-setAP-hostapd.html "RPi-setAP-hostapd") to get some clues.
4. Add RPiBoat.py into /etc/rc.local, or make other changes to set it starting when system boots.

You are more than welcomed to email me when encountering issues.
