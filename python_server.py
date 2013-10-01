from socket import *
from threading import Thread

HOST = "localhost"
PORT = 8000

def clientHandler():
    conn, addr = s.accept()
    print addr, "is Connected"
    while 1:
        data = conn.recv(1024)
        data = eval(data)
        if not data:
            break
        print repr(data[0]),': ', repr(data[1])
    


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print "Server is running...."

for i in range(5):
    Thread(target=clientHandler).start()

s.close()
