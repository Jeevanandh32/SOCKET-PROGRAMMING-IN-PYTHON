Here is an inch-by-inch explanation of the server code that complements the client-side
application.

import socket
import threading
● socket: This module allows the creation of sockets (TCP/IP) to enable
communication between computers (or in this case, between client and server
programs).
● threading: This module is used to run multiple threads concurrently. Each client
connection will be handled by a separate thread, allowing multiple clients to connect
simultaneously.

def handle_client(conn, addr):
print(f"New connection from {addr}")
● handle_client: This function is responsible for handling communication between
the server and a connected client.
● conn: The connection object representing the client. It allows the server to send and
receive data from this specific client.
● addr: The address of the client (IP address and port number).
● The print statement logs that a new client has connected, using the client's
address.

conn.sendall("Welcome to the math server!".encode())
● conn.sendall: Sends data to the connected client. Here, the server sends a
"Welcome to the math server!" message.
● .encode(): Converts the string into bytes (since sockets deal with byte streams, not
strings).

husky_name = conn.recv(1024).decode().strip()
● conn.recv(1024): Receives up to 1024 bytes of data from the client.
● .decode(): Converts the received bytes back into a string.
● .strip(): Removes any leading or trailing whitespace or newline characters from
the string.
● This line receives the client's introduction (e.g., "HELLO ravi.j") sent by the client.

if husky_name.startswith("HELLO"):
print(f"Received intro from {husky_name.split()[1]}")
● if husky_name.startswith("HELLO"): This checks whether the received
message starts with the word "HELLO". This ensures that the client has correctly
introduced itself.
● husky_name.split()[1]: Splits the introduction message by spaces and extracts
the second part, which should be the Husky username (e.g., "ravi.j").
● print: Logs the Husky username to the server console.

questions = [
"MATH 12 + 23",
"MATH 45 - 12",
"MATH 9 * 8",
"MATH 56 / 7"
]
● questions: This is a list of math problems that the server will send to the client.
Each question follows the format "MATH num1 operator num2".

for question in questions:
conn.sendall(f"{question}\n".encode())
● for question in questions:: This loop iterates over each question in the list
of questions.
● conn.sendall(f"{question}\n".encode()): For each question, the server
sends the math problem to the client. The \n ensures that the message is followed
by a newline, and .encode() converts the message to bytes before sending.

answer = conn.recv(1024).decode().strip()
print(f"Received: {answer}")
● After sending each math problem, the server waits to receive the client's answer.
● answer = conn.recv(1024).decode().strip(): Receives the client's
response, decodes it, and removes extra whitespace.
● print(f"Received: {answer}"): Logs the received answer to the server
console.

flag = f"FLAG-{addr[1]}-{husky_name.split()[1]}"
conn.sendall(f"DONE {flag}\n".encode())
● After all the math questions have been answered, the server creates a unique flag for
the client.
● flag = f"FLAG-{addr[1]}-{husky_name.split()[1]}": Constructs a
unique flag string. It combines the client's port number (addr[1]) and their Husky
username (husky_name.split()[1]).
● conn.sendall(f"DONE {flag}\n".encode()): Sends the "DONE" message,
followed by the flag, to the client, signaling the end of the session.

conn.close()
● conn.close(): Closes the connection with the client. This releases any resources
allocated to the connection and ensures that the server is ready for a new client.
The main server function

def start_server():
HOST = '127.0.0.1'
PORT = 8888
● start_server: This function initializes and runs the server.
● HOST: Specifies the IP address the server will listen on. Here, 127.0.0.1 is the
loopback address, which means the server only accepts connections from the same
machine.
● PORT: The port number the server will listen on. Here, it is set to 8888.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
● socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a new
socket.
○ socket.AF_INET: Indicates that the socket will use the IPv4 protocol.
○ socket.SOCK_STREAM: Indicates that the socket will use the TCP protocol
(as opposed to UDP).

server.bind((HOST, PORT))
● server.bind((HOST, PORT)): Binds the server to the specified IP address
(HOST) and port number (PORT), so it knows where to listen for incoming
connections.

server.listen(5)
print(f"Server listening on {HOST}:{PORT}")
● server.listen(5): Puts the server into listening mode. The argument 5 specifies
the maximum number of queued connections (clients) that can wait to be accepted at
once.
● print(f"Server listening on {HOST}:{PORT}"): Logs to the console that
the server is now listening for connections on the specified address and port.

while True:
conn, addr = server.accept()
● while True: This infinite loop ensures that the server keeps running indefinitely,
accepting multiple client connections.
● conn, addr = server.accept(): When a client tries to connect, the server
accepts the connection. conn represents the connection object, and addr is the
client's address (IP and port).

thread = threading.Thread(target=handle_client, args=(conn,
addr))
thread.start()
● thread = threading.Thread(target=handle_client, args=(conn,
addr)): A new thread is created to handle the client. The handle_client function
is passed as the target, with the conn and addr arguments. This allows each client
to be handled concurrently without blocking other clients.
● thread.start(): Starts the newly created thread. Now the server can accept and
handle multiple clients at the same time.

if __name__ == "__main__":
start_server()
● if __name__ == "__main__":: This ensures that the start_server function is
called only if the script is executed directly, not imported as a module.
● start_server(): Calls the start_server function, starting the server process.

Summary
This server listens on a specific IP (127.0.0.1) and port (8888), accepts incoming client
connections, and handles each client in a separate thread. For each client, it sends math
problems, receives answers, and finally sends a unique flag before closing the connection.
This setup allows the server to handle multiple clients concurrently.

