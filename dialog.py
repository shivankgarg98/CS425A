
import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")
def create_window():
    window = tk.Toplevel(root)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

new = tk.Button(frame, text="Create new window", command=create_window)
new.pack(side=tk.LEFT)

red_pen = tk.Button(frame,
                   text="Red Pen",
                   bg = "red",
                   command=write_slogan)
red_pen.pack(side=tk.LEFT)

black_pen = tk.Button(frame, text="Black Pen", bg = "gray1", fg ="snow",command=write_slogan)
black_pen.pack(side=tk.LEFT)

eraser = tk.Button(frame, text="Eraser", command=write_slogan)
eraser.pack(side=tk.LEFT)

exit = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
exit.pack(side=tk.LEFT)

while 1:
    root.update()
    root.update_idletasks()





