from tkinter import *
root=Tk()

def key_pressed(event):
    w=Label(root,text="Key Pressed:"+event.char)
    w.place(x=70,y=90)

some_canvas = Canvas(root)
some_canvas.pack()
some_canvas.bind("<Key>",key_pressed)
some_canvas.mainloop()