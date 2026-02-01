import socket, threading, json

HOST_IP = ""  #listen on all available interfaces
PORT = 65432
HOUSE_FILE = "house.json"
conn_clients = []

#Read house.json file
def load_house_state():
  with open(HOUSE_FILE, 'r') as f:
    data = json.load(f)
  return data

#open json file for write
def new_house_state(state: dict):
  with open(HOUSE_FILE, 'w') as f:
    json.dump(state, f, indent=4)
    print("House state updated: ", state)

#Parse key:value, & upd. json file"
#returns True if at least 1 valid key was updated.
def update_house_fr_msg(message: str) -> bool:
  state = load_house_state()
  updated = False

#divide key:value pairs by comma
  parts = message.split(",")
  for part in parts:
    part = part.strip()
    if ":" not in part:
      continue

    key, value = part.split(":", 1)
    key = key.strip()
    value = value.strip()

    if key in state:
      state[key] = value
      updated = True
    
    if updated:
      new_house_state(state)
  return updated

#broadcast a message to all connected clients
def broadcast(message):
  for client in conn_clients:
    try:
      client.sendall(message.encode())
    except:
      pass #ignore broken connections

#handle client connection
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

          updated = update_house_fr_msg(text)
          if updated:
            print(f"House state updated from Client {thread_id}: {text}")
            response = f"House state updated successfully on server from Client {thread_id}."
          else:
            response = f"Server received from Client {thread_id}: {text} (no state updates)."
          
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
    print(f"Server is listening for all interfaces on port :{PORT}")
    print("Server IP:", socket.gethostbyname(socket.gethostname()))

    house_state = load_house_state()  #read file when servern starts
    print(f"Current house state: {house_state}\n")

    while True:
      conn, addr = s.accept() #addr = address of client that is connecting, conn = new socket to interact with the client

      thread_count += 1
      thread_id = thread_count

      print(f"[NEW CLIENT] {addr} connected.\n")

      thread = threading.Thread(target=handle_client, args=(conn, addr, thread_id), daemon=True)

      thread.start()
      print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") #-1 to not count the main thread

if __name__ == "__main__":
  main()