### Import BWT encoder module ###
import sys
import os

# Get absolute path of project directory 
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)                # get project root 
components_path = os.path.join(project_root, 'Components') # get components path

sys.path.insert(0, components_path)
sys.path.insert(0, project_root) 

from Components.bwt_calculator import encoder as bwt

# Import Socket and Threading modules
import socket as sck
import threading as thr

# Client handler function
def client_handle(conn, addr):

    with conn:
        print(f"Connected with {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            print(f"Received string: {data.decode()} from {addr}")

            encoded_string = bwt(data.decode())

            conn.send(encoded_string.encode())

# Server socket settings
HOST = "127.0.0.1"
PORT = 65432

# Socket opening
with sck.socket(family = sck.AF_INET, type = sck.SOCK_STREAM) as s:

    s.bind( (HOST, PORT) )

    s.listen()

    print(f"Server listening on {HOST}:{PORT}...")

    while True:

        conn, addr = s.accept()
        
        t1 = thr.Thread(target=client_handle, args=(conn, addr))
        t1.start()
        
        





