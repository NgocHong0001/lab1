# 2 - Client initiates a connection

import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))  # connect to the server
  print(f"Connected to server at {HOST}:{PORT}")


# 3 - Data is echanged
  s.sendall(b"Hello, server")  # send data to the server b= 8bit units
  data = s.recv(1024)          # receive echoed data from the server

print(f"Received {data!r} from the server")