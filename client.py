import socket
import threading 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("input port connection")
connectPort = int(input())

Nickname = input("Choose a nickname")

client.connect(("127.0.0.1", connectPort ))

def fileRecieve(message):
    try:
        name = message.split()[1]
        file = open(f"Received/{name}", "wb")

        packet = client.recv(2048)

        while packet:
            file.write(packet)
            packet = client.recv(2048)

        file.close()
        print("file recieved")

    except:
        client.send("ERROR".encode("ascii"))
def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "Send nickname" :
                client.send(Nickname.encode("ascii"))

            elif message.split()[0]  == "SendFile":
                print("sending file")

                fileTransfer(message)

            elif message[0] == '/':
                fileRecieve(message)


                
            else:
                print(message)


        except:
            print("ERROR")
            client.close()
            print("CONNECTION ENDED")
            break

def write():
    while True:
        imp = input('')
        if imp == "/quit":
            quit()
        message = f"{Nickname}: {imp}"
        client.send(message.encode("ascii"))

def fileTransfer(message): #/send dt-1333.jpg
    try:
        file = open(f"Send/{message.split()[1]}", "rb")

        packet = file.read(2048)

        while packet:
            client.send(packet)
            packet = file.read(2048)
            

        packet = 'done'.encode('ascii')
        client.send(packet)
        file.close()
        print("file sent")



    except:
        print("ERROR")
        client.send('error'.encode("ascii"))

receiveThread = threading.Thread(target=receive)

receiveThread.start()


writeThread = threading.Thread(target=write)

writeThread.start()