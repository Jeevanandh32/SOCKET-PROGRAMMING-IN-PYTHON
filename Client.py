import socket
import sys

def solve_math(question):
    _, num1, op, num2 = question.split()
    num1, num2 = int(num1), int(num2)

    if not (0 < num1 < 100 and 0 < num2 < 100):
        print("Error: Numbers must be one or two digits.")
        return "INVALID"
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  # Integer division

def run_client():
    HOST = '127.0.0.1'
    PORT = 8888
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.settimeout(10)  # Set a 10-second timeout
            
            # Receive welcome message
            welcome = s.recv(1024).decode().strip()
            print(f"Server: {welcome}")
            
            # Send introduction
            husky_name = input("Enter your Husky username: ")
            intro = f"HELLO {husky_name}\n"
            print(f"Sending: {intro.strip()}")
            s.sendall(intro.encode())
            
            while True:
                data = s.recv(1024).decode().strip()
                print(f"Server: {data}")
                
                if data.startswith("DONE"):
                    print(f"Received flag: {data.split()[1]}")
                    break
                elif data.startswith("MATH"):
                    answer = solve_math(data)
                    response = f"ANSWER {answer}\n"
                    print(f"Sending: {response.strip()}")
                    s.sendall(response.encode())
                elif not data:
                    print("No data received. Exiting.")
                    break
        
        except socket.timeout:
            print("Socket timeout occurred. Exiting.")
        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_client()
