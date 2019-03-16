#!/usr/bin/python

"""
PiBoat socket server
"""

from SocketServer import ThreadingTCPServer, StreamRequestHandler
import traceback
import time


class MyRequestHandler(StreamRequestHandler):
    """
    #从BaseRequestHandler继承，并重写handle方法
    """

    def handle(self):
        print "Got Connections!"
        while True:
            try:
                data = self.rfile.readline().strip()
                if data != '':
                    print "receive from (%r):%r" % (self.client_address, data)
                    time.sleep(0.05)
                    self.wfile.write(data.upper())
                    print "Respond Successfully!"
                # self.client_address是客户端的连接(host, port)的元组
            except:
                traceback.print_exc()
                self.finish()
                break


if __name__ == "__main__":
    # telnet 127.0.0.1 9999
    host = ""  # 主机名，可以是ip,像localhost的主机名,或""
    port = 8888  # 端口
    addr = (host, port)

    # 购置TCPServer对象，
    server = ThreadingTCPServer(addr, MyRequestHandler)

    # 启动服务监听
    server.serve_forever()
