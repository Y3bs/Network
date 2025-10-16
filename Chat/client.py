from concurrent.futures import thread
import socket, threading
import os, asyncio, sys

os.system('cls')
nickname = input("Enter your nickname: ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",55555))
asyncio.sleep(5)
os.system('cls')

def receive():
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            if msg == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(msg)
        except:
            print("Connection Error. Check your code")
            client.close()
            break

def write():
    while True:
        msg = f"{nickname}: {input("")}"
        client.send(msg.encode("ascii"))
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")   
        sys.stdout.flush()

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
