import tkinter as tk
from assets import *
import os
import math
import pickle 

#Settings
run_height = 700
run_width = 900
run_size = str(run_width) + "x" + str(run_height)
pencil_size = 1
eraser_size = 5

#Open Window
root = tk.Tk()
root.geometry(run_size)
root.title("Sketch v0")



#--------------Basic Drawing Functions---------------------

# This function colours a singular pixel on the canvas
def graphite(stroke, point, colour):
    x = point[0]
    y = point[1]
    stroke.coverage.append(Userspace.create_rectangle(x,y,x,y,fill=colour))
    stroke.coverage_points.append((x,y))
    Userboard.link_point(x,y, stroke)


# uses graphite() to colour a small dot
def round_point(stroke, center, radius, colour="black"):
    for i in range(center[0]-radius,center[0]+radius+1):
        for j in range(center[1]-radius,center[1]+radius+1):
            if (i - center[0])**2 + (j - center[1])**2 <= radius**2:
                    graphite(stroke,(i,j), colour)


# uses graphite to colour an area
def pencil_tip(stroke, center,radius,colour="black"):
    for i in range(center[0]-radius,center[0]+radius):
        for j in range(center[1]-radius,center[1]+radius):
            graphite(stroke,(i,j), colour)


#--------------Event Handling---------------------------
# global variables are used so that events can share data
Userboard = Board(run_width,run_height)
global last_point
global pencil_mode
global stroke_record
stroke_record = Userboard.stroke_list
pencil_mode = "draw"


def on_hold_down(event):
    global last_point
    global stroke_record

    x, y = event.x, event.y
    if pencil_mode == "draw":
        
        displacement = (x - last_point[0], y - last_point[1])
        displacement_magnitude_square = displacement[0]**2 + displacement[1]**2

        if displacement_magnitude_square > 4:
            displacement_magnitude = math.sqrt(displacement_magnitude_square)
            for i in range(int(displacement_magnitude)):
                unit = (displacement[0]/displacement_magnitude, displacement[1]/displacement_magnitude)
                pencil_tip(stroke_record[-1], (int(last_point[0] + i*unit[0]), int(last_point[1] + i*unit[1])), pencil_size)
            

        pencil_tip(stroke_record[-1], (x,y), pencil_size)
        last_point = (x,y)
    elif pencil_mode == "erase":
        for i in Userboard.get_point(x,y).linked_strokes:
            if i in Userboard.get_point(x,y).linked_strokes:
                Userboard.delete_stroke(i)


def on_tap(event):
    global last_point
    global stroke_record
    x, y = event.x, event.y
    if pencil_mode == "draw":
        #create a stroke object
        stroke_record.append(Stroke("black", Userspace))

        
        last_point = (x,y)
        round_point(stroke_record[-1], (x,y), pencil_size)
    elif pencil_mode == "erase":
        for i in Userboard.get_point(x,y).linked_strokes:
            Userboard.delete_stroke(i)


def on_release(event):
    global stroke_record
    if pencil_mode == "draw":
        x, y = event.x, event.y

        round_point(stroke_record[-1], (x,y), pencil_size)

def on_erase():
    global pencil_mode
    pencil_mode = "erase"


def on_pencil():
    global pencil_mode
    pencil_mode = "draw"
    
    garbage = True
    while garbage:
        try:
            Userboard.stroke_list.remove(None)
        except:
            garbage = False

def on_debug():
    print(Userboard.stroke_list)

def new_file():
    pass
def save():
    destination = "Saves\save1.huf"
    metadata = SaveObject(Userboard)
    savefile = open(destination,"wb")
    pickle.dump(metadata, savefile)
    savefile.close()
def open_file():
    source = "Saves\save1.huf"
    savefile = open(source,"rb")
    metadata = pickle.load(savefile)
    for i in metadata.strokes:
        Userboard.load_stroke(i,Userspace)
def export():
    pass

global destination
def project_selected(event):
    global destination
    selectedindices = Projects_listbox.curselection()
    selection = Projects_listbox.get(selectedindices[0])
    destination = "Saves\\" + selection
    
def project_open():
    global destination
    source = destination
    savefile = open(source,"rb")
    metadata = pickle.load(savefile)
    for i in metadata.strokes:
        Userboard.load_stroke(i,Userspace)

def new_project():
    pass






    

#Main Menu
main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As...", command=save)
file_menu.add_command(label="Export", command=export)
edit_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
view_menu = tk.Menu(main_menu)
main_menu.add_cascade(label="View", menu=view_menu)
root.config(menu=main_menu)

#Canvas and related interface
canvas_column_span = 3

Userspace = tk.Canvas(root, height=(run_height) - 15, width=run_width-200, bg='#D8E0FF')
Userspace.grid(row=1,column=0, columnspan=canvas_column_span,rowspan=2)

EraserButton = tk.Button(root, text="Eraser", font=("Arieal", 10), command=on_erase)
EraserButton.grid(row=0,column=0)

PencilButton = tk.Button(root, text="Pencil", font=("Arieal", 10), command=on_pencil)
PencilButton.grid(row=0,column=1)

DebugButton = tk.Button(root, text="Debug", font=("Arieal", 10), command=on_debug)
DebugButton.grid(row=0,column=2)

Projects_label = tk.Label(root, text = 'Projects', font=("Ariel",15))
Projects_label.grid(row=0, column=canvas_column_span, columnspan=2)
Projects_menu = tk.Scrollbar(root)
Projects_menu.grid(row=1,column=canvas_column_span+1)
Projects_listbox = tk.Listbox(root, yscrollcommand=Projects_menu.set)
Projects_list = os.listdir("Saves\\")
for i in Projects_list:
    Projects_listbox.insert(tk.END, i)
Projects_listbox.grid(row=1,column=canvas_column_span,columnspan=2)
Projects_menu.config(command=Projects_listbox.yview)
Projects_listbox.bind('<<ListboxSelect>>',project_selected)

OpenButton = tk.Button(root, text="Open",command=project_open)
OpenButton.grid(row=2,column=canvas_column_span)

NewButton = tk.Button(root, text="+",command=new_project)
NewButton.grid(row=2,column=canvas_column_span+1)







Userspace.bind('<B1-Motion>', on_hold_down)
Userspace.bind('<Button-1>', on_tap)
Userspace.bind('<ButtonRelease-1>', on_release)

root.mainloop()