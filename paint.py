from tkinter import *
import numpy as np
import socket 
import select 
import sys 
import json
from tkinter.colorchooser import *

color=(1,'red')
def getColor():
    global color
    color = askcolor() #choose your color
    button1.configure(bg = color[1]) #dynamic update the color you ask
    w.configure(cursor="crosshair") #change the canvas cursor to crosshair for painting"

def eraser():
    global color
    color = (2,'#d9d9d9')
    w.configure(cursor="spraycan") #change cursor to indicate deletion

def naya(event):
    global xp 
    global yp
    global wid
    xp, yp = ( event.x ), ( event.y )
    wid=min(w.winfo_width(),w.winfo_height())

def paint(event):
    global xp 
    global yp
    global wid
    global hi
    x, y = ( event.x  ), ( event.y  )
    w.create_line( xp, yp, x, y ,width=float(scale.get()), fill=color[1])
    coord=[xp,yp,x,y,wid]
    pen_width = float(scale.get())
    pen = [color,pen_width]
    data = {"coordinates":coord,"pen_params":pen}
    server.send(bytes(json.dumps(data),'utf8'))
    xp, yp = ( event.x  ), ( event.y  )

#Button(text='Select Color', command=getColor).pack()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))

sockets_list = [sys.stdin, server] 

read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
server.settimeout(0.001)
canvas_width = 500
canvas_height = 150
xp=0
yp=0
master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.configure(cursor="crosshair")
w.bind( "<B1-Motion>", paint )
w.bind( "<Button-1> ", naya)
wid=min(w.winfo_width(),w.winfo_height())

button1 = Button(text = "PEN COLOR", command = getColor, anchor = W)
button1.configure(width = 10, activebackground = "#33B5E5", relief = RAISED, bg = color[1])
button1_window = w.create_window(10, 10, anchor=NW, window=button1)

scale = Scale(master, from_=1, to=15, orient=HORIZONTAL)
scale.pack()
eraser = Button(text = 'ERASER', command = eraser, anchor = W)
eraser.configure(width = 10, activebackground = "#33B5E5", relief = RAISED, bg='snow')
eraser_window = w.create_window(10,50, anchor=NW, window=eraser)


message = Label( master, text = "You know what to do now" )
message.pack( side = BOTTOM )
while 1:
    for socks in read_sockets: 
        if socks == server:
            try: 
                mes = socks.recv(2048)
                mes=mes.decode()
                print(mes)
                if(mes[1]=='W'):
                    continue
                else:
                    mes=json.loads(mes)
                    print(mes)  
                cords = mes['data']['coordinates']
                pen_params = mes['data']['pen_params']
                if(len(cords)):
                    w.create_line( cords[0]*wid/cords[4], cords[1]*wid/cords[4], cords[2]*wid/cords[4], cords[3]*wid/cords[4] ,width=pen_params[1], fill=pen_params[0][1])
            except socket.timeout:
                '''  print('')'''    
    master.update_idletasks()
    master.update()
#mainloop()
server.close()
