import socket

#create a server side socket using IPV4 (AF_INET) & TCP (SOCKET_STREAM)

#IP = socket.gethostbyname(socket.gethostname())
#HOST = socket.gethostname()
#PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  #print(socket.gethostname()) #get hostname of machine
  #print(socket.gethostbyname(socket.gethostname())) #get ip address of machine
  s.bind((socket.gethostbyname(socket.gethostname()), 65432)) #bind socket to hostname & port
  s.listen() #listen for connections
  print("Server is listening for connections...")

#Listen forever to accepts ANY connection
  while True:
    #accept every single connection & store two pieces of information
    conn, addr = s.accept() #addr = address of client that is connecting, conn = new socket to interact with the client
    #print(type(conn)) #socket object
    #print(conn)
    #print(type(addr)) #tuple
    #print(addr) #('ip address', port)

    print(f"Connected to {addr}!\n")

    #Send a message to a client that just connected
    conn.sendall(b"Hello client, you are connected to the server!")
    conn.close() #close the connection with the client
    break  #remove break to keep server running for multiple connections