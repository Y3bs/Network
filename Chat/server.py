from operator import add
from this import d
import socket, threading
import os
import socket

def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


host = "0.0.0.0"
port = 55555
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()


clients = []
nicknames = []


def broadcast(msg):
    for client in clients:
        client.send(msg)
    
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            idx = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[idx]
            broadcast(f"{nickname} left the chat".encode("ascii"))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, addr = server.accept()
        print(f"Connected to {str(addr)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        broadcast(f"{nickname} joined the chat".encode("ascii"))
        nicknames.append(nickname)
        clients.append(client)

        print(f"Client Nickname: {nickname}")
        client.send("Connected. You joined the chat".encode("ascii"))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
if __name__ == "__main__":
    os.system('cls')
    print(f"Server IP: {ip()}")
    print("Server is listening.... ")
    receive()

