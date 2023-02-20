import tkinter as tk

placement_record = []

class PointLocation:
    def __init__(self,x_loc,y_loc):
        self.x = x_loc
        self.y = y_loc
        self.linked_strokes = []
    
    def __repr__(self):
        return str((self.x,self.y))
    
    def link_stroke(self,stroke_address):
        self.linked_strokes.append(stroke_address)


#The implementation of Board could cause a bug where data isn't saved properly
class Board:
    def __init__(self, x_size,y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.stroke_list = []
        self.points = []
        for i in range(self.y_size):
            for j in range(self.x_size):
                self.points.append(PointLocation(j,i))
    
    def print_board(self):
        for i in range(self.y_size):
            row = []
            for j in range(i*self.x_size, i*self.x_size + self.x_size):
                row.append(self.points[j])
            print(row)

    def get_point(self, x, y):
        return self.points[y*self.x_size + x]

    def link_point(self, x, y, stroke_adress):
        self.points[y*self.x_size + x].link_stroke(stroke_adress)
    
    def delete_stroke(self, stroke_address):
        stroke_address.erase_coverage()
        self.stroke_list.remove(stroke_address)
    

        

class Stroke:
    def __init__(self, colour, Userspace):
        self.Userspace = Userspace
        self.colour = colour
        self.coverage = []
    #Userspace is only defined in main.py, this will not work if the canvas is not named Userspace
    def erase_coverage(self):
        for i in self.coverage:
            self.Userspace.delete(i)


if __name__ == "__main__":
    Userboard = Board(20,20)
    