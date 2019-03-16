#!/usr/bin/python
# -*- encoding: UTF-8 -*-


from SocketServer import ThreadingTCPServer, StreamRequestHandler
import traceback
import threading
import os
import sys
from pi_pwm import PiPWM

timer_interval = 2

class Connection_Watcher(threading.Thread):
    def __init__(self):
        print "Loading Watcher..."
        threading.Thread.__init__(self)

    def run(self):
        while True:


class MyStreamRequestHandlerr(StreamRequestHandler):
    def handle(self):
        # t = threading.Timer(5.0, self.sayhello)
        # t.start()
        print "Incoming Connection!"

        while True:
            try:
                data = self.rfile.readline().strip()
                if data != '':
                    print ("receive from (%r):%r" % (self.client_address, data))
                    response = data + '\n'
                    self.wfile.write(response.upper())  # respond to phones to make sure realiable connections
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
        print ("hello")
        self.wfile.write("hello")
        global t  # Notice: use global variable!
        t = threading.Timer(2.0, self.sayhello)
        t.start()


if __name__ == "__main__":
    host = ""  # 主机名
    port = 23333  # 端口
    addr = (host, port)
    try:
        pwm = PiPWM()
        server = ThreadingTCPServer(addr, MyStreamRequestHandlerr)
        print "Server Started Successfully! Waiting Connections!"
        server.serve_forever()
    except KeyboardInterrupt:
        pass
        print "Server shutting down..."
    server.server_close()
    pwm.stop()
    print "Done!"

