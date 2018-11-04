from tkinter import *

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
   xp, yp = ( event.x  ), ( event.y  )

master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height, bg="#fff")
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )
w.bind( "<Button-1> ", naya)

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
	
mainloop()