import socket
import time
import random

server_name = "Shahar_server"
# create the server
server_sot = socket.socket()
server_sot.bind(("0.0.0.0",1450))
server_sot.listen(3)

while True:
    #server waits fo clients
    client_sot, addr = server_sot.accept()
    print(f"{addr[0]} - connected")
    while True:
        try:
            data = client_sot.recv(4).decode()
        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break

        print(f"getting data - {data}")
        if data == "TIME":
            msg  = time.strftime("%H:%M:%S")

        elif data == "NAME":
            msg = server_name
        elif data == "RAND":
            msg = str(random.randint(1, 11))
        else:
            break

        client_sot.send(str(len(msg)).zfill(2).encode())
        client_sot.send(msg.encode())

    print(f"{addr[0]} - disconnected")
    client_sot.close()