import socket
 
HOST = 'localhost'
PORT = 9999
# BUFSIZ = 102400
ADDR = (HOST, PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)
 
while True:
 
    data = raw_input('> ')
    if not data:
            break
    tcpCliSock.send("%s\r\n"%data)