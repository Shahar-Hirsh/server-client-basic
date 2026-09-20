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
            print(f"getting data - {data}")
            if data == "TIME":
                current_time = time.strftime("%H:%M:%S")
                client_sot.send(str(len(current_time)).zfill(2).encode())
                client_sot.send(current_time.encode())
            elif data == "NAME":
                client_sot.send(str(len(server_name)).zfill(2).encode())
                client_sot.send(server_name.encode())
            elif data == "RAND":
                rnd = str(random.randint(1, 11))
                client_sot.send(str(len(rnd)).zfill(2).encode())
                client_sot.send(rnd.encode())
            else:
                msg = "Bye Bye"
                client_sot.send(str(len(msg)).zfill(2).encode())
                client_sot.send(msg.encode())
                break

        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break

    print(f"{addr[0]} - disconnected")
    client_sot.close()