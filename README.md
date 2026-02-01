🏠 House State Client–Server Project
📌 Project Description

This project demonstrates a TCP client–server system where multiple clients can connect to a server and update the state of a house (light, door, window).
The house state is stored in a JSON file and visualized using a Tkinter GUI on the server side.

The project is designed to show:

Client–server communication using sockets

Communication across different computers on the same network

Parsing messages and updating shared state

Basic GUI updates without blocking the event loop

🧠 System Overview

Server

Runs on one computer

Listens for incoming client connections

Receives messages such as light:off, door:closed

Updates House.json

Displays the current house state in a GUI

Client

Runs on the same or a different computer

Connects to the server using the server’s IP address

Sends commands to update the house state

📂 Project Structure
project/
│
├── server.py        # TCP server with multiclient support
├── client.py        # TCP client
├── House.json       # Stores current house state
├── gui.py (if used) # Tkinter GUI for visualization
└── README.md

🗂 House.json Format

The house state is stored as key–value pairs:

{
  "light": "on",
  "door": "open",
  "window": "open"
}


Each key represents a device, and the value represents its current state.

🔌 Network Setup

The server runs on one computer and uses its local network IP address (e.g. 192.168.0.23)

The client connects using that IP address and a predefined port

Both computers must be connected to the same Wi-Fi network

This demonstrates communication between different machines instead of using localhost.

🔄 Message Format

Clients send messages in the following format:

key:value, key:value


Example:

light:off, door:closed


Only existing keys in House.json are updated. Invalid keys are ignored.

🖼 GUI Update Logic

The GUI reads House.json repeatedly using root.after()

The file is reloaded each time to reflect external updates

A while loop is not used to avoid blocking the Tkinter event loop

✅ Key Concepts Demonstrated

TCP sockets (AF_INET, SOCK_STREAM)

Multiclient server using threads

JSON read/write (json.load, json.dump)

Message parsing and validation

Tkinter GUI updates using after()

Separation of logic (networking, state, GUI)

▶ How to Run
1. Start the Server
python server.py

2. Start the Client (same or different computer)
python client.py


Enter the server’s IP address when prompted.

🎯 Learning Outcome

This project demonstrates how a client can communicate with a server on another computer, update shared data stored in a JSON file, and reflect those changes in a graphical interface.
