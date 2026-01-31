import socket, threading

#HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 65432


#create a client side IPV4 socket (AF_INET) and TCP (SOCK_STREAM)
#no close() needed when using with statement.

def main():
  host_ip = input(f"Enter server IP address: ").strip() #get server IP from user

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host_ip, PORT)) #connect the socket to a server located at a given IP & PORT
    print(f"Connected to server at {host_ip}:{PORT}\n")

    #listen for Hi message from server
    server_resp = s.recv(1024).decode()
    print(f"Received from server: {server_resp}")
    
    #write message to server
    message = input("-> ") #take input fr. user

    while message.lower().strip() != 'bye':
      
      s.send(message.encode()) #send data to the server (must be encoded to bytes)

      response = s.recv(1024).decode() #recv. resp. fr. server & decode it to string
      print(f"Received from server: {response}")

      message = input("-> ") #take input fr. client again

if __name__ == "__main__":
  main()