import socket

#create a client side IPV4 socket (AF_INET) and TCP (SOCK_STREAM)
#no close() needed when using with statement.

HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST_IP, PORT)) #connect the socket to a server located at a given IP & PORT

  print(f"Connected to server at {HOST_IP}:{PORT}")
  
  #write message to server
  message = input("-> ") #take input fr. user

  while message.lower().strip() != 'bye':
    s.send(message.encode()) #send data to the server (must be encoded to bytes)
    data = s.recv(1024).decode() #recv. resp. fr. server & decode it to string
    print("Received from server: ",data) 
    message = input("-> ") #take input fr. client again