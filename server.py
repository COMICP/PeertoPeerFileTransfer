import threading 
import socket
import random


port = 50000#random.randint(50000, 60000)

commandList = ( #keep list of commands here to send to user when help is needed. 
    "/? = Command list ", 
    "/send ''FileName'' ''UserName'' = Send file to user ", 
    "/dist ''FileName'' = Send file to everyone"
    )


IPAddress = '127.0.0.1' #local host
print(f"Port number = {int(port)} \nIP Address = {IPAddress}")

#Replace section above with section below for non local use

#hostname = socket.gethostname()
#IPAddress = socket.gethostbyname(hostname)
#print(f"Port number = {int(port)}\n IP Address = {IPAddress} \nHost Name = {hostname}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IPAddress, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def userCommand(client, message):
    
    if message.split()[1] == "/?":
        client.send(str(commandList).encode("ascii"))

    elif message.split()[1] == "/send":
        getFile(client, message)

    else:
        client.send("unknown command".encode("ascii"))


def getFile(client, message):
    
    try:
        name = message.split()[2]
        file = open(f"serverstore/{name}", "wb")

        client.send(f"SendFile {name}".encode("ascii")) 
        packet = client.recv(2048)

        while packet:
            file.write(packet)

            packet = client.recv(2048) #never exits loop even though packets stop coming


            

        file.close()
        print("file recieved")

        broadcastFile(name)

    except:
        client.send("ERROR".encode("ascii"))
        print("error")





def handle(client):
    while True:
        try:
            
            message = client.recv(1024)

            if message.decode("ascii").split()[1][0] == "/":
                userCommand(client, message.decode("ascii")) #passes message as string and client profile
                message = message.decode("ascii")[0]+" used a command"
            
            broadcast(message)

                
            
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has disconnected".encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"'{str(address)}' joined")

        client.send("Send nickname".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"client nickname - {nickname}")
        broadcast(f"{nickname} joined".encode("ascii"))
        client.send(f"Welcome {nickname}".encode('ascii'))

        thread = threading.Thread(target= handle, args= (client,))
        thread.start()

def broadcastFile(name):
    print(f"broadcasting file {name}")
    try:
        
        for client in clients:
            file = open(f"serverstore/{name}", "rb")
            packet = file.read(2048)
            client.send(f"/ {name}".encode("ascii"))
            

            while packet:
                
                client.send(packet)
                packet = file.read(2048)


            
            print("file sent to " + client)
        print("files sent")
        file.close()
        return
    
    except:
        print("ERROR")

recieve()