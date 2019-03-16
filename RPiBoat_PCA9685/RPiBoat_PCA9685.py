#!/usr/bin/python2
# -*- encoding: UTF-8 -*-


from SocketServer import ThreadingTCPServer, StreamRequestHandler
import traceback
import threading
import os
import sys
#import re
#import subprocess
from pi_pwm_for_PCA9685 import PiPWM

timer_interval = 2

controller_ip = "192.168.10.240"

class ConnectionWatcher(threading.Thread):
    def __init__(self):
        print "Connection Checker Loading..."
        threading.Thread.__init__(self)
    def run(self):
        while(True):
            try:
                print "Checking..."
                #p = subprocess.Popen(["sudo ping -i 0.1 -w 2 -c 2 192.168.10.240"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                #out=p.stdout.read()
                #print out
                #regex = re.compile('100%')
                #if len(regex.findall(out))!=0:
                p = os.system("sudo ping -i 0.1 -w 2 -c 2 " + controller_ip) # This Line will block the thread.
                if not p:
                    pwm.emergency_stop()
                    print "Shutting dowm motor..."
                else:
                    print "Everything Normal!"
            except:
                print "Can Not Check Connections!"

class CommandHandler(StreamRequestHandler):
    def handle(self):
        # t = threading.Timer(5.0, self.sayhello)
        # t.start()
        print "Incoming Connection!"
        if not ('t' in dir()):
            sayhello()
        if not ('Con' in dir()):
            Con = ConnectionWatcher()
            Con.start()
        while True:
            try:
                data = self.rfile.readline().strip()
                if data != '':
                    print ("receive from (%r):%r" % (self.client_address, data))
                    response = data + '\n'
                    self.wfile.write(response.upper())
                    if data == "reboot":
                        os.system('reboot')
                        sys.exit()
                    elif data == "halt":
                        os.system("shutdown -r -t 5 now")
                        sys.exit()
                    elif data == "rtsp":
                        os.system(
                            "raspivid -o - -w 640 -h 360 -t 9999999 |cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264 & ")
                    elif data[0:2] == 'm1':
                        print("---" + data.upper())
                        pwm.motor_set(float(data.split(",")[1]))  # 电机速度设置

                    elif data[0:2] == 's1':
                        print("---" + data.upper())
                        pwm.servo1_set(float(data.split(",")[1]))  # 舵机设置
            except KeyboardInterrupt:
                traceback.print_exc()
                self.server.shutdown()
                break

            except:
                traceback.print_exc()
                self.finish()
                break

    def sayhello(self):  # 定时握手 维持连接
        print ("Hello")
        self.wfile.write("Hello")
        global t  # Notice: use global variable!
        t = threading.Timer(2.0, self.sayhello)
        t.start()


if __name__ == "__main__":
    host = ""  # 主机名
    port = 23333  # 端口
    addr = (host, port)
    try:
        pwm = PiPWM()
        server = ThreadingTCPServer(addr, CommandHandler)
        print "Server Started Successfully! Waiting Connections!"
        server.serve_forever()
    except KeyboardInterrupt:
        pass
        print "Server shutting down..."
    server.server_close()
    pwm.stop()
    print "Done!"

