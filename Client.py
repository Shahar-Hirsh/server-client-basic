import socket


my_sock = socket.socket()
# connect to server
try:
    my_sock.connect(("127.0.0.1",1450))
except Exception as e:
    my_sock.close()
    exit(f"server is down - try again {str(e)}")

while True:
    msg = input("enter msg to send - ").upper()
    if msg not in ["TIME", "NAME", "RAND", "EXIT"]:
        print("not a valid input - try again")
        continue

    try:
        my_sock.send(msg.encode())
        data_len = int(my_sock.recv(2).decode())
        data = my_sock.recv(data_len).decode()
        print(f"server send - {data}")

        if msg == "EXIT":
            break

    except Exception as e:
        print(f"error in receive or sending data {str(e)}")
        break

my_sock.close()
