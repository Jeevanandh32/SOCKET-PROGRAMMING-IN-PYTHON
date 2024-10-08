Here is an inch-by-inch breakdown of the client-side Python code, which connects to a server, solves mathematical problems sent by the server, and communicates back with the server.

Imports

import socket import sys

socket: This module is required to create and work with network connections using sockets (both TCP and UDP). In this case, we are working with a TCP socket. sys: Provides access to system-specific parameters and functions. Here, it is imported but not explicitly used.

Math-Solving Function

def solve_math(question): _, num1, op, num2 = question.split() num1, num2 = int(num1), int(num2)

solve_math: This function takes a mathematical question sent by the server as a string (e.g., "MATH 12 + 23"). question.split(): The input string is split into four components: the keyword "MATH", two numbers (num1 and num2), and an operator (op). num1, num2 = int(num1), int(num2): Converts the numbers from strings to integers for computation.

if not (0 < num1 < 100 and 0 < num2 < 100): print("Error: Numbers must be one or two digits.") return "INVALID"

Ensures that both num1 and num2 are within the range 1–99. If they aren’t, an error message is printed, and the function returns "INVALID" to indicate the question doesn’t meet the problem’s constraint.

if op == '+': return num1 + num2 elif op == '-': return num1 - num2 elif op == '*': return num1 * num2 elif op == '/': return num1 // num2 # Integer division

This section performs the appropriate mathematical operation based on the operator op: +: Addition -: Subtraction *: Multiplication /: Integer division using // to avoid decimal results. The computed result is returned to the caller.

Client-Side Socket Setup and Connection

def run_client(): HOST = '127.0.0.1' PORT = 8888

run_client: The main function that starts the client. HOST: Defines the IP address the client connects to. 127.0.0.1 is the loopback address (local machine), meaning the client is communicating with a server running on the same machine. PORT: The port number the client will connect to (here, 8888).

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a new socket. AF_INET: Specifies IPv4 as the address family. SOCK_STREAM: Specifies TCP as the transport protocol. with: Ensures that the socket (s) is properly closed after the block of code is executed, even if an exception occurs.

Connection Establishment and Data Handling

   try:
        s.connect((HOST, PORT))
        s.settimeout(10)  # Set a 10-second timeout
s.connect((HOST, PORT)): Establishes a connection to the server at the specified IP address and port. s.settimeout(10): Sets a timeout of 10 seconds for all blocking operations on the socket. This prevents the client from waiting indefinitely if the server doesn’t respond.

       welcome = s.recv(1024).decode().strip()
        print(f"Server: {welcome}")
s.recv(1024): Receives up to 1024 bytes of data from the server. This data is expected to be in byte format. .decode().strip(): Converts the received bytes to a string and removes any leading or trailing whitespace. The welcome message from the server is printed to the console.

Sending the Husky Username to the Server

       husky_name = input("Enter your Husky username: ")
        intro = f"HELLO {husky_name}\n"
        print(f"Sending: {intro.strip()}")
        s.sendall(intro.encode())
input(): Prompts the user to enter their Husky username. intro = f"HELLO {husky_name}\n": Constructs a greeting message to introduce the client to the server. s.sendall(intro.encode()): Sends the introduction message to the server. .encode() converts the string into bytes.

Receiving and Processing Server Messages while True: data = s.recv(1024).decode().strip() print(f"Server: {data}")

while True:: A loop that continuously listens for messages from the server. s.recv(1024): Waits to receive up to 1024 bytes of data from the server. data: The decoded message from the server is stored in data. print(f"Server: {data}"): Prints the message received from the server to the console.

Handling Different Server Messages

           if data.startswith("DONE"):
                print(f"Received flag: {data.split()[1]}")
                break
if data.startswith("DONE"): Checks if the server has sent a "DONE" message, which signals the end of the session. data.split()[1]: Extracts the second part of the message, which is the unique flag generated by the server. break: Breaks the loop and exits the program.

           elif data.startswith("MATH"):
                answer = solve_math(data)
                response = f"ANSWER {answer}\n"
                print(f"Sending: {response.strip()}")
                s.sendall(response.encode())
elif data.startswith("MATH"): Checks if the server has sent a math problem (message starts with "MATH"). answer = solve_math(data): Calls the solve_math function to compute the answer. response = f"ANSWER {answer}\n": Constructs the response message in the format "ANSWER result". s.sendall(response.encode()): Sends the computed answer back to the server.

           elif not data:
                print("No data received. Exiting.")
                break
If no data is received from the server, the client prints an exit message and breaks out of the loop, closing the connection.

Exception Handling

   except socket.timeout:
        print("Socket timeout occurred. Exiting.")
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")
socket.timeout: If a timeout occurs (the server doesn't respond in 10 seconds), an error message is printed, and the client exits. ConnectionRefusedError: If the server is not running or refuses the connection, this error is caught. Exception: Any other exceptions are caught and the error is printed.

Main Block

if name == "main": run_client()

This block ensures that the run_client function is only executed if the script is run directly (not imported as a module). It starts the client process.

Summary The client connects to a server, introduces itself with a Husky username, receives math problems, solves them, and sends the answers back. It handles errors such as timeouts and connection refusal gracefully. When the session is done, it receives a unique flag from the server and exits.

Here is an inch-by-inch explanation of the server code that complements the client-side application.

import socket import threading ● socket: This module allows the creation of sockets (TCP/IP) to enable communication between computers (or in this case, between client and server programs). ● threading: This module is used to run multiple threads concurrently. Each client connection will be handled by a separate thread, allowing multiple clients to connect simultaneously.

def handle_client(conn, addr): print(f"New connection from {addr}") ● handle_client: This function is responsible for handling communication between the server and a connected client. ● conn: The connection object representing the client. It allows the server to send and receive data from this specific client. ● addr: The address of the client (IP address and port number). ● The print statement logs that a new client has connected, using the client's address.

conn.sendall("Welcome to the math server!".encode()) ● conn.sendall: Sends data to the connected client. Here, the server sends a "Welcome to the math server!" message. ● .encode(): Converts the string into bytes (since sockets deal with byte streams, not strings).

husky_name = conn.recv(1024).decode().strip() ● conn.recv(1024): Receives up to 1024 bytes of data from the client. ● .decode(): Converts the received bytes back into a string. ● .strip(): Removes any leading or trailing whitespace or newline characters from the string. ● This line receives the client's introduction (e.g., "HELLO ravi.j") sent by the client.

if husky_name.startswith("HELLO"): print(f"Received intro from {husky_name.split()[1]}") ● if husky_name.startswith("HELLO"): This checks whether the received message starts with the word "HELLO". This ensures that the client has correctly introduced itself. ● husky_name.split()[1]: Splits the introduction message by spaces and extracts the second part, which should be the Husky username (e.g., "ravi.j"). ● print: Logs the Husky username to the server console.

questions = [ "MATH 12 + 23", "MATH 45 - 12", "MATH 9 * 8", "MATH 56 / 7" ] ● questions: This is a list of math problems that the server will send to the client. Each question follows the format "MATH num1 operator num2".

for question in questions: conn.sendall(f"{question}\n".encode()) ● for question in questions:: This loop iterates over each question in the list of questions. ● conn.sendall(f"{question}\n".encode()): For each question, the server sends the math problem to the client. The \n ensures that the message is followed by a newline, and .encode() converts the message to bytes before sending.

answer = conn.recv(1024).decode().strip() print(f"Received: {answer}") ● After sending each math problem, the server waits to receive the client's answer. ● answer = conn.recv(1024).decode().strip(): Receives the client's response, decodes it, and removes extra whitespace. ● print(f"Received: {answer}"): Logs the received answer to the server console.

flag = f"FLAG-{addr[1]}-{husky_name.split()[1]}" conn.sendall(f"DONE {flag}\n".encode()) ● After all the math questions have been answered, the server creates a unique flag for the client. ● flag = f"FLAG-{addr[1]}-{husky_name.split()[1]}": Constructs a unique flag string. It combines the client's port number (addr[1]) and their Husky username (husky_name.split()[1]). ● conn.sendall(f"DONE {flag}\n".encode()): Sends the "DONE" message, followed by the flag, to the client, signaling the end of the session.

conn.close() ● conn.close(): Closes the connection with the client. This releases any resources allocated to the connection and ensures that the server is ready for a new client. The main server function

def start_server(): HOST = '127.0.0.1' PORT = 8888 ● start_server: This function initializes and runs the server. ● HOST: Specifies the IP address the server will listen on. Here, 127.0.0.1 is the loopback address, which means the server only accepts connections from the same machine. ● PORT: The port number the server will listen on. Here, it is set to 8888.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ● socket.socket(socket.AF_INET, socket.SOCK_STREAM): Creates a new socket. ○ socket.AF_INET: Indicates that the socket will use the IPv4 protocol. ○ socket.SOCK_STREAM: Indicates that the socket will use the TCP protocol (as opposed to UDP).

server.bind((HOST, PORT)) ● server.bind((HOST, PORT)): Binds the server to the specified IP address (HOST) and port number (PORT), so it knows where to listen for incoming connections.

server.listen(5) print(f"Server listening on {HOST}:{PORT}") ● server.listen(5): Puts the server into listening mode. The argument 5 specifies the maximum number of queued connections (clients) that can wait to be accepted at once. ● print(f"Server listening on {HOST}:{PORT}"): Logs to the console that the server is now listening for connections on the specified address and port.

while True: conn, addr = server.accept() ● while True: This infinite loop ensures that the server keeps running indefinitely, accepting multiple client connections. ● conn, addr = server.accept(): When a client tries to connect, the server accepts the connection. conn represents the connection object, and addr is the client's address (IP and port).

thread = threading.Thread(target=handle_client, args=(conn, addr)) thread.start() ● thread = threading.Thread(target=handle_client, args=(conn, addr)): A new thread is created to handle the client. The handle_client function is passed as the target, with the conn and addr arguments. This allows each client to be handled concurrently without blocking other clients. ● thread.start(): Starts the newly created thread. Now the server can accept and handle multiple clients at the same time.

if name == "main": start_server() ● if name == "main":: This ensures that the start_server function is called only if the script is executed directly, not imported as a module. ● start_server(): Calls the start_server function, starting the server process.

Summary This server listens on a specific IP (127.0.0.1) and port (8888), accepts incoming client connections, and handles each client in a separate thread. For each client, it sends math problems, receives answers, and finally sends a unique flag before closing the connection. This setup allows the server to handle multiple clients concurrently.
