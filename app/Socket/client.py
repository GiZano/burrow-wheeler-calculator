import socket as sck

HOST = "127.0.0.1"
PORT = 65432

with sck.socket(family = sck.AF_INET, type = sck.SOCK_STREAM) as s:

    s.connect( (HOST, PORT) )

    s.send(b"BANANA")

    data = s.recv(1024)

    print(f"Transformed: {data.decode()}")
