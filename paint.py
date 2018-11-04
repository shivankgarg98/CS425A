from tkinter import *
import socket 
import select 
import sys 
  
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

def naya (event):
	global xp 
	global yp
	xp, yp = ( event.x  ), ( event.y  )
def paint( event ):
   global xp 
   global yp
   x, y = ( event.x  ), ( event.y  )
   print(x,y)
   w.create_line( xp, yp, x, y ,width=5)
   message=str(xp)+'|'+str(yp)+'|'+str(x)+'|'+str(y)
   server.send(bytes(message,'utf8'))
   xp, yp = ( event.x  ), ( event.y  )

master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
w.bind( "<Button-1> ", naya)

message = Label( master, text = "You know what to do now. :-P" )
message.pack( side = BOTTOM )
while 1:
   for socks in read_sockets: 
        if socks == server:
            try: 
               mes = socks.recv(2048)
               mes=mes.decode()
               cords=[]
               if(mes[0]=='<'):
                  mes=mes.split('>')[1]
                  mes=mes.split('|')
                  for i in mes:
                     cords.append(int(i))
               print(cords)
               if(len(cords)):
                  w.create_line( cords[0], cords[1], cords[2], cords[3] ,width=5)
            except socket.timeout:
               print('')    
   master.update_idletasks()
   master.update()
#mainloop()
server.close()
