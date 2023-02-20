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
        self.linked_strokes.append = stroke_address


#The implementation of Board could cause a bug where data isn't saved properly
class Board:
    def __init__(self, x_size,y_size):
        self.x_size = x_size
        self.y_size = y_size

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

    def index(self,x,y):
        return self.points[y*self.x_size + x]
        

class Stroke:
    def __init__(self, colour):
        self.colour = colour
        self.coverage = []

if __name__ == "__main__":
    Userboard = Board(20,20)
    #Userboard.print_board()
    print(Userboard.index(19,19))
    print(Userboard.index(0,0))
    print(Userboard.index(17,15))
    