import socket
import time

conn = socket.create_connection()
sk = socket.socket()

ip_port = ('127.0.0.1', 99999)
sk.bind(ip_port)
sk.listen(5)

for i in range(10):

    = sk.accept()
    client_data = conn.recv(1024)
    time.sleep(1)

    print(time.ctime() + " | " + client_data)

