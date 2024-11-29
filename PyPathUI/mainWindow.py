from tkinter import Tk, Button, Canvas, Frame, BOTH

from PyPath.aStar import AStar

from PyPathUI.cellUI import CellUI
from PyPathUI.robotUI import RobotUI

import time

class pathCanvas(Frame):

    def __init__(self, a_x:int = 800, a_y: int = 600, a_cell_width = 50, a_cell_height = 50):
        super().__init__()

        self._m_x = a_x
        self._m_y = a_y
        self._m_cell_width = a_cell_width
        self._m_cell_height = a_cell_height

        self._m_cells = {}

        self._m_robot_start_cell = None
        self._m_robot_end_cell = None

        self.initUI()

    def button(self, event):
        l_cell = self.getNearestCell(event.x, event.y)

        if l_cell:
            if l_cell.isOccupied():
                l_cell.free()
            else:
                l_cell.occupied()

    def getNearestCell(self, a_x: int , a_y: int):
        l_col = a_x // self._m_cell_width
        l_row = a_y // self._m_cell_height

        return self._m_cells[l_col][l_row]

    def initUI(self):
        self.master.title("PathFinder :)")
        self.pack(fill=BOTH, expand=1)

        self._m_canvas = Canvas(self)

        for l_col_index in range(0, self.max_col_index+1):
            for l_row_index in range(0, self.max_row_index+1):
                self._m_cells.setdefault(l_col_index, {})[l_row_index] = CellUI(self._m_canvas, l_col_index, l_row_index, self._m_cell_width, self._m_cell_height, self.max_col_index, self.max_row_index)

        self._m_robot = RobotUI(self._m_canvas, 10,10,10)

        self.reInit()

        self._m_canvas.pack(fill=BOTH, expand=1)

    @property
    def max_col_index(self):
        return (self._m_x-1) // self._m_cell_width
    
    @property
    def max_row_index(self):
        return (self._m_y-1) // self._m_cell_height

    def findPath(self):
        l_path = AStar(self._m_robot_start_cell, self._m_robot_end_cell, self._m_cells, self.max_col_index, self.max_row_index)

        if not isinstance(l_path, list):
            print("No path found!")
        else:
            for l_element in l_path:
                l_element.setColor('pink')
    
    def reInit(self):
        for l_col_index in range(0, self.max_col_index+1):
            for l_row_index in range(0, self.max_row_index+1):
                self._m_cells[l_col_index][l_row_index].free()

        self._m_robot_start_cell = self._m_cells[0][0]
        self._m_robot_end_cell = self._m_cells[self.max_col_index][self.max_row_index]

        self._m_robot_start_cell.setColor('green')
        self._m_robot_end_cell.setColor('green')                

    @staticmethod
    def start():
        root = Tk()
        ex = pathCanvas(800, 600, 20, 20)
        root.geometry("800x700+300+300")

        l_find_path_button = Button(root, text="FindPath", command=ex.findPath)

        l_find_path_button.pack(side='bottom')

        l_reset_button = Button(root, text="Reset", command=ex.reInit)

        l_reset_button.pack(side='bottom')

        # Mouse click tracking
        root.bind('<Button-3>', ex.button)

        root.mainloop()