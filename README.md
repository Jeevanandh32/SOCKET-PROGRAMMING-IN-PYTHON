### SOCKET PROGRAMMING IN PYTHON

This repository contains a project showcasing socket programming in Python, focusing on building efficient client-server communication. The project is designed to demonstrate key concepts in networking, such as creating sockets, establishing connections, sending and receiving data, and closing sockets.

### Features
- Client-Server Communication: Facilitates data exchange between a client and server using TCP/IP protocol.
- Multi-Threaded Server: Handles multiple client connections simultaneously, ensuring scalability.
- Customizable: Easily adaptable to different networking scenarios by modifying parameters such as IP address, port, and data payload.
- Error Handling: Includes robust error-handling mechanisms for unexpected disconnections or invalid inputs.

### Prerequisites
- Python 3.x installed on your system.
- Basic understanding of networking concepts, including TCP/IP and sockets.

### Getting Started

### Clone the Repository
```
git clone https://github.com/Jeevanandh32/SOCKET-PROGRAMMING-IN-PYTHON.git
cd SOCKET-PROGRAMMING-IN-PYTHON
```

### Install Dependencies
No additional dependencies are required beyond Python's built-in libraries.

### Run the Server
```
python server.py
```

### Run the Client
In a new terminal window:
```
python client.py
```

You can run multiple clients to test the server's multi-threading capabilities.

### How It Works
1. The server creates a socket, binds it to a specific IP and port, and listens for incoming connections.
2. Clients create sockets to connect to the server and initiate communication.
3. Both client and server exchange messages, demonstrating real-time data transfer over the network.
4. The connection is gracefully terminated once the communication is complete.

### Example Use Case
- Real-time messaging applications.
- File transfer systems.
- Basic simulations of client-server architectures.

### Files
- server.py: Contains the code to run the server.
- client.py: Contains the code to run the client.
- README.md: Documentation for the project.

### Contributions
Feel free to fork this repository and submit pull requests for any improvements or additional features.

### License
This project is licensed under the MIT License.
