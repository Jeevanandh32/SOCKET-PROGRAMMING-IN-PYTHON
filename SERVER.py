import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    conn.sendall("Welcome to the math server!".encode())
    
    husky_name = conn.recv(1024).decode().strip()
    if husky_name.startswith("HELLO"):
        print(f"Received intro from {husky_name.split()[1]}")
        questions = [
            "MATH 12 + 23",
            "MATH 45 - 12",
            "MATH 9 * 8",
            "MATH 56 / 7"
        ]
        
        for question in questions:
            conn.sendall(f"{question}\n".encode())
            answer = conn.recv(1024).decode().strip()
            print(f"Received: {answer}")
        
        flag = f"FLAG-{addr[1]}-{husky_name.split()[1]}"
        conn.sendall(f"DONE {flag}\n".encode())
    
    conn.close()

def start_server():
    HOST = '127.0.0.1'
    PORT = 8888
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
