import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(c)
c.connect(("10.0.0.149", 9300))
name = input("Input 5 numbers separated by space:")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())
