import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 2137)
print ("Connecting to {}".format(server_address))
sock.connect(server_address)

try:
    while True:
        data = sock.recv(1024)
        if "END" in data.decode():
            break
        print(data.decode())
        if "ENTER" not in data.decode():
            message = ""
            while len(message) == 0:
                message = input()
        else:
            message = input()
        sock.send(str.encode(message))
finally:
    print(data.decode())
    print("Closing connection...")
    sock.close()