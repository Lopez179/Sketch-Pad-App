import tkinter as tk

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
        for i in range(len(self.stroke_list)):
            if self.stroke_list[i] == stroke_address:
                self.stroke_list[i] = None
    
    def load_stroke(self, StrokeSave, Userspace):
        current_stroke = Stroke(StrokeSave.colour, Userspace)
        self.stroke_list.append(current_stroke)
        for i in StrokeSave.coverage_points:
            current_stroke.coverage.append(Userspace.create_rectangle(i[0],i[1],i[0],i[1],fill=StrokeSave.colour))
            self.link_point(i[0],i[1],self.stroke_list[-1])
        current_stroke.coverage_points = StrokeSave.coverage_points
            
    
class Stroke:
    def __init__(self, colour, Userspace):
        self.Userspace = Userspace
        self.colour = colour
        self.coverage = []
        self.coverage_points = []

    def erase_coverage(self):
        for i in self.coverage:
            self.Userspace.delete(i)
        self.coverage_points.clear()


class StrokeSave:
    def __init__(self, colour, coverage_points):
        self.coverage_points = coverage_points
        self.colour = colour


class SaveObject:
    def __init__(self, board):
        self.strokes = []
        for i in board.stroke_list:
            self.strokes.append(StrokeSave(i.colour, i.coverage_points))
        
    



if __name__ == "__main__":
    Userboard = Board(20,20)
    