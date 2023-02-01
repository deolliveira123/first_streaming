import socket as sck
import time

HOST = "localhost"
PORT = 3000

s = sck.socket()
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)


    