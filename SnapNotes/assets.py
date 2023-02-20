import tkinter as tk

placement_record = []

#The implementation of Board could cause a bug where data isn't saved properly
class Board:
    def __init__(self, x_size,y_size):
        self.x_size = x_size
        self.y_size = y_size

        self.rows = []
        for i in range(x_size):
            this_row = []
            for j in range(y_size):
                point = (i,j)
                colour = "None"
                this_row.append((point,colour))
            self.rows.append(this_row)

    def print_contents(self):
        for i in self.rows:
            print(i)

    def get_point(self,point):

        return self.rows[point[0]][point[1]]

    def set_point(self,point, colour):
        self.rows[point[0]][point[1]] = (point, colour)
        

class Stroke:
    def __init__(self, colour):
        self.colour = colour
        self.coverage = []

if __name__ == "__main__":
    Userboard = Board(20,20)
    print(Userboard.get_point((5,4)))
    Userboard.set_point((5,4),"black")
    print(Userboard.get_point((5,4)))