import socket
import threading

# HOST = '172.20.10.13'
PORT = 5050

# list and dictionary to hold clients who join the server
clients = []
usernames = {}

# initialise the server socket and nimd it to listen on he ip address and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',PORT))

server.listen()

# function to broadcast message received from one client to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# fucntion to receive message sent by clients
def handle(client):
    while True:
        try:    
            message = client.recv(2048)

            decode = message.decode('utf-8')

            if decode == '!exit':
                break

            broadcast(message)
        except:
            pass

# safely removes client when the leave the chat 
    if client in clients:
        username = usernames[client]

# broadcasts a message to clients when someone leaves the chat
        broadcast(f"{username} has left the chat.".encode('utf-8'))
        print(f'{username} left the chat')
        clients.remove(client)
        del usernames[client]
    client.close()

# function to accept clients when they are joining the server 
def receive():

# this loop listens to accepet clients onto the server  
    while 1:
        client,address = server.accept()
        print(f'connected successfully to {address}')

# receives the user name if client and saves it in the username dictionary and also the client address
        username = client.recv(2048).decode('utf-8')
        if username != '':
            usernames[client] = username
            clients.append((client)) 
        else:
            print('username required')
            exit()

# broadcasts a message that clients have joined the chat with the username
        print (f'{username} joined the server')
        broadcast(f'{username} joined the chat'.encode('utf-8'))
        # client.send('connected to the server'.encode('utf-8'))

# this thread keeps the receive function listening for incoming requests
        thread = threading.Thread(target=handle ,args=(client,)).start()

receive()

