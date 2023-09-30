# Overview

This framework provides a simple Client/Server interaction using TCP over a local network. 

The program is broken into 2 separate files. The first is the server file. To use the server file simply run the program. On boot the server will display the port and ip address. For this service, the server only acts as a middleman and has no commands for itself. The second file is the client. Launch this in the same way to start the program. After opening, the client asks for a name and a port number. After entering these, it will connect to the server. From here anything submitted to the console will be displayed to all clients connected to the server. The exception to this is commands. Commands for this program are denoted by beginning with “/” then the keywords. The only commands implemented currently are SendFile and Quit. /quit ends the program and terminates the connection. /SendFile “filename” will take the file of that name from the send folder and send it to all clients in the server. The file will be found in the received folder on completion. 

The purpose of this program is to create an easily upgradable base for Client/Server chat rooms. In order to add future functionality, the command structure is made to be modular.


[Software Demo Video](https://youtu.be/MRH3OW_mJ2g)

# Network Communication

This program uses a client / server model.

Connection made using TCP, port number selected at random when server instance is run. Port number printed in server console. 

Text messages encoded in “ascii”

File transfer 

# Development Environment

* Windows 10 pro
* Visual studio code
* Python extension v2023.16.0

{Describe the programming language that you used and any libraries.}

# Useful Websites

* [Idiot Developer](https://idiotdeveloper.com/large-file-transfer-using-tcp-socket-in-python/)
* [Real Python](https://realpython.com/python-sockets/)
* [Wikipedia - Client server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [Wikipedia - OSI model](https://en.wikipedia.org/wiki/OSI_model)

# Future Work

* Extend command list to include different options on user interaction
* Set up GUI
* Implement file explorer pop up for file selection
* Finalize file transfer and fix non exiting loops
