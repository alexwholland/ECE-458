import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")
print(s)
s.bind(('10.0.0.149', 9300))
s.listen()
print('waiting for connections')
while True:
    c, addr = s.accept()
    # Decode the message and store the values into a list
    clientInput = c.recv(1024).decode().split()
    # Convert client number into integers
    clientInput = [int(i) for i in clientInput]
    clientInput.sort()
    print('connected with', addr)

    if len(clientInput) != 5:
        c.send(bytes('Please make sure you ONLY type 5 numbers', 'utf-8'))
        c.close()
    c.send(bytes(f'The smallest value is: {clientInput[0]}, '
                 f'the largest value is: {clientInput[4]}', 'utf-8'))
    c.close()
