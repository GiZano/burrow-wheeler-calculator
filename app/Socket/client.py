# Import socket library
import socket as sck

# Server connection settings
HOST = "127.0.0.1"
PORT = 65432

# Socket creation
with sck.socket(family = sck.AF_INET, type = sck.SOCK_STREAM) as s:

    # Connection to server
    s.connect( (HOST, PORT) )

    # Get the string to encode from the user
    to_transform = str(input("Insert string to encode:"))

    # Send the transformation request
    s.send(to_transform.encode())

    # Received the transformed string
    data = s.recv(1024)

    # Print out the result
    print(f"Transformed: {data.decode()}")
