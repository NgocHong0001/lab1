import socket

# 1. Server sets up for listening socket
HOST = "localhost"
PORT = 65432

#addr = client & server negotioate a new port to use for their interaction, it returns a socket address pair. (interaction address of the client)

#conn = new socket, will interact with the address returned -> addr (incl. port socket will use) a new socket object used to send / recieve data in this connection)

#with statement automatically closes the socket when done

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
  s.bind((HOST, PORT))
  s.listen() #listen to the request fr. the server fr. socket
  print(f"Server listen on {HOST}:{PORT}...")
  conn, addr = s.accept() # pause & waiting to accept a connection aka blocking (no other prog. will take place until a connection is accepted) 

#Data exchanged
  with conn:
    print(f"Connected by {addr}")
    while True:
      data = conn.recv(1024) # receive data fr. the client (max 1024 bytes)
      if not data:
        break
      conn.sendall(data)  # echo back the received data to the client