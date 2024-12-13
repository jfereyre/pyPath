from tkinter import Canvas, Frame, BOTH


from PyPathUI.cellUI import CellUI, CellMatrixUI
from PyPathUI.robotUI import RobotUI
from PyPath.cell import CellMatrix

class PathCanvas(Frame):

    def __init__(self, a_x:int, a_y: int, a_cells: CellMatrix):
        super().__init__()

        self._m_x = a_x
        self._m_y = a_y
        self._m_cell_width = self._m_x // a_cells.max_col_index
        self._m_cell_height = self._m_y // a_cells.max_row_index

        self._m_cells = a_cells

        self._m_robot_start_cell = self._m_cells.get(0,0)
        self._m_robot_end_cell = self._m_cells.get(self._m_cells.max_col_index-1, self._m_cells.max_row_index-1)

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

        return self._m_cells.get(l_col, l_row)

    def initUI(self):
        self.master.title("PathFinder :)")
        self.pack(fill=BOTH, expand=1)

        self._m_cells_matrix_ui = CellMatrixUI(self._m_cells, self, 800, 600)
        self._m_robot = RobotUI(self._m_cells_matrix_ui, 10,10,10)

        self.reInit()

        self._m_cells_matrix_ui.pack(fill=BOTH, expand=1)

    @property
    def max_col_index(self):
        return ((self._m_x-1) // self._m_cell_width)-1
    
    @property
    def max_row_index(self):
        return ((self._m_y-1) // self._m_cell_height)-1

    @property
    def cell_height(self):
        return self._m_cell_height
    
    @property
    def cell_width(self):
        return self._m_cell_width

    def displayPath(self, a_path: list):
        for l_element in a_path:
            l_element.setColor('pink')
    
    def reInit(self):
        self.releaseOccupied()

        self._m_robot_start_cell = self._m_cells_matrix_ui.get(0,0)
        self._m_robot_end_cell = self._m_cells_matrix_ui.get(self._m_cells.max_col_index-1, self._m_cells.max_row_index-1)

        self._m_robot_start_cell.setColor('green')
        self._m_robot_end_cell.setColor('green')           

    def releaseOccupied(self):
        for l_col_index in range(0, self.max_col_index):
            for l_row_index in range(0, self.max_row_index):
                self._m_cells.get(l_col_index,l_row_index).free()

    def setCellOccupied(self, a_x:int, a_y: int):
        self._m_cells.get(a_x,a_y).occupied()

    def setRobotPosition(self, a_x: int, a_y: int):
        self._m_robot.move(a_x, a_y)

