import socket, threading

HOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 65432
conn_clients = []

def broadcast(message):
  for client in conn_clients:
    try:
      client.sendall(message.encode())
    except:
      pass #ignore broken connections

def handle_client(conn, addr, thread_id):
  print(f"[CLIENT {thread_id}] connected from {addr}.\n")

  conn_clients.append(conn) #save clients
  broadcast(f"Hi from Server!\n")
  
  try: 
    with conn:
        welcome_msg = f"Welcome Client {thread_id}!"
        conn.send(welcome_msg.encode())

        while True:
          msg = conn.recv(1024) #receive data from the client wont accept data > 1024 bytes

          if not msg:
            print(f"Connection with {addr} closed (client disconnected).")
            break

          text = msg.decode()
          if text.lower().strip() == 'bye':
            print(f"Connection with {addr} closed by client 'bye' command.")
            break

          response = f"Server received from Client {thread_id}: {text}"
          conn.send(response.encode()) #send data to the client
  except ConnectionResetError:
    print(f"Connection with {addr} lost (connection reset).")

  if conn in conn_clients:
    conn_clients.remove(conn) #remove client on disconnect
  print(f"[DISCONNECTED] {addr} disconnected.")

#create a server side IPV4 socket (AF_INET) and TCP (SOCK_STREAM)
def main():
  thread_count = 0

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #print(socket.gethostname()) #get hostname of machine
    #print(socket.gethostbyname(socket.gethostname())) #get ip address of machine

    s.bind((HOST_IP, PORT)) #bind socket to hostname & port

    s.listen() #listen for connections
    print(f"Server is listening for connections on {HOST_IP}:{PORT}...")

    while True:
      conn, addr = s.accept() #addr = address of client that is connecting, conn = new socket to interact with the client

      thread_count += 1
      thread_id = thread_count

      print(f"[NEW CLIENT] {addr} connected.")

      thread = threading.Thread(target=handle_client, args=(conn, addr, thread_id), daemon=True)

      thread.start()
      print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") #-1 to not count the main thread

      #conn.close() #close connection with the client CHECKED!!
    
    

if __name__ == "__main__":
  main()