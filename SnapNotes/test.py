import tkinter as tk
from assets import *
from ctypes import windll
import os
import pickle as pck

#Settings
run_height = 300
run_width = 500
run_size = str(run_width) + "x" + str(run_height)
pencil_size = 1

#Open Window
root = tk.Tk()
root.geometry(run_size)
root.title("SmartSketch v0")

#Get Program Working
Userboard = Board(run_width,run_height)

#Program Functions
def graphite(point,colour="black"):
    x = point[0]
    y = point[1]
    Userspace.create_rectangle(x,y,x,y,fill=colour)
    placement_record.append((x,y))

def pencil_tip(center,radius,colour="black"):
    frame_length = radius*2
    for i in range(center[0]-radius,center[0]+radius+1):
        for j in range(center[1]-radius,center[1]+radius+1):
            if (i - center[0])**2 + (j - center[1])**2 <= radius**2:
                graphite((i,j), colour)


def on_stroke(event):
    x, y = event.x, event.y

    pencil_tip((x,y), pencil_size)

def on_tap(event):
    x, y = event.x, event.y

    pencil_tip((x,y), pencil_size)


Userspace = tk.Canvas(root, height=(run_height) - 30, width=run_width)
Userspace.grid(row=1,column=0)

Userspace.bind('<B1-Motion>', on_stroke)
root.bind('<Button-1>', on_tap)


root.mainloop()



