import socket

#create a client side IPV4 socket (AF_INET) and TCP (SOCK_STREAM)
#no close() needed when using with statement.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((socket.gethostbyname(socket.gethostname()), 65432)) #connect the socket to a serber located at a given IP & PORT
  
  #Recieve a message fr. the server...must specify the max nbr of bytes to recv.
  message = s.recv(1024) #1024 bytes max
  print(message) 