import socket
import sys
import time
import select
import pyaudio
from _thread import *

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=20000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

p=pyaudio.PyAudio()
recv_stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,output=True,frames_per_buffer=CHUNK)
send_stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

def recv_data():
    while True:
        try:
            data = s.recv(1024)
            receive_stream.write(data)
        except:
            pass


def send_data():
    while True:
        try:
            data = send_stream.read(CHUNK)
            s.sendall(data)
        except:
            pass

start_new_thread(recv_data, ())
start_new_thread(send_data, ())
  
while True: 
    pass
