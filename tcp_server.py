import socket

#server with 1 client
#create a server side socket using IPV4 (AF_INET) & TCP (SOCKET_STREAM)

HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #print(socket.gethostname()) #get hostname of machine
  #print(socket.gethostbyname(socket.gethostname())) #get ip address of machine

  s.bind((HOST_IP, PORT)) #bind socket to hostname & port

  s.listen() #listen for connections

  print("Server is listening for connections...")

  conn, addr = s.accept() #addr = address of client that is connecting, conn = new socket to interact with the client
  

  with conn:
    print(f"Connected to {addr}!\n")
    while True:
      data = conn.recv(1024) #receive data from the client wont accept data > 1024 bytes
      if not data:
        break
      print(f"Received from client: {data.decode()}\n")
      data_input = input("-> ")
      conn.send(data_input.encode()) #send data to the client