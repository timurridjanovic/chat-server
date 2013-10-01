from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
username = raw_input("Your username: ")
while 1:
    message = raw_input("Your Message: ")
    toSend = str((username, message))
    s.send(toSend)

s.close()
