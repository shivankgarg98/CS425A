
# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from _thread import *
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 

IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.bind((IP_address, Port)) 
server.listen(100) 

list_of_clients = [] 

def clientthread(conn, addr):  
    mes= {'type':'message',
            'message':'Welcome',
            'data':'',
            'addr':''}
    conn.send(bytes('|'+json.dumps(mes),'utf8')) 
    while True: 
        try: 
            message = conn.recv(2048) 
            if message: 
                msg=message.decode()
                print(msg)
                msg=json.loads(msg)
                mes=json.dumps({"type":"draw", "addr":addr[0],"data":msg})
                mes='|'+mes
                broadcast(mes, conn) 
            else: 
                remove(conn) 

        except: 
            continue

def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(bytes(message,'utf8') )
            except: 
                clients.close() 

                                # if the link is broken, we remove the client 
                remove(clients) 

def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 

while True: 
    conn, addr = server.accept() 

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn) 
        # prints the address of the user that just connected 
    print(addr[0] + " connected")

        # creates and individual thread for every user  
        # that connects 
    start_new_thread(clientthread,(conn,addr))     

conn.close() 
server.close()
