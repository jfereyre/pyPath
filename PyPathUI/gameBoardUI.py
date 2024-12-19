from tkinter import Frame, BOTH


from PyPathUI.cellUI import CellMatrixUI
from PyPathUI.robotUI import RobotUI
from PyPath.cell import CellMatrix
from PyPath.robot import Robot

class GameBoardUI(Frame):

    def __init__(self, a_width:int, a_height: int, a_cells: CellMatrix, a_robot: Robot):
        super().__init__()

        self._m_width = a_width
        self._m_height = a_height
        self._m_cell_width = self._m_width // (a_cells.max_col_index+1)
        self._m_cell_height = self._m_height // (a_cells.max_row_index+1)

        self._m_cells = a_cells
        self._m_robot = a_robot

        self._m_cells_matrix_ui = CellMatrixUI(self._m_cells, self, self._m_width, self._m_height)
        self._m_robot_ui = RobotUI(self._m_robot, self._m_cells_matrix_ui, self._m_cell_width // 2)

        self.master.title("PathFinder :)")
        self.pack(fill=BOTH, expand=1)

        self.reInit()

        self._m_cells_matrix_ui.pack(fill=BOTH, expand=1)

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

    @property
    def max_col_index(self):
        return ((self._m_width-1) // self._m_cell_width)-1
    
    @property
    def max_row_index(self):
        return ((self._m_height-1) // self._m_cell_height)-1

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
        l_robot_start_position = self._m_robot.getStartPosition()
        l_robot_destination = self._m_robot.getDestination()

        self._m_robot_start_cell = self._m_cells_matrix_ui.get(l_robot_start_position[0], l_robot_start_position[1])
        self._m_robot_end_cell = self._m_cells_matrix_ui.get(l_robot_destination[0], l_robot_destination[1])

        self._m_robot_start_cell.setColor('green')
        self._m_robot_end_cell.setColor('green')           

    def releaseOccupied(self):
        for l_col_index in range(0, self.max_col_index):
            for l_row_index in range(0, self.max_row_index):
                self._m_cells.get(l_col_index,l_row_index).free()

    def setCellOccupied(self, a_x:int, a_y: int):
        self._m_cells.get(a_x,a_y).occupied()

    def setRobotPosition(self, a_x: int, a_y: int):
        self._m_robot_ui.move(a_x, a_y)

    def setRobotStartCell(self, a_col: int, a_row: int):
        self._m_robot_start_cell = self._m_cells.get(a_col,a_row)

    def getRobotStartCell(self):
        return self._m_robot_start_cell

    def setRobotEndCell(self, a_col: int, a_row: int):
        self._m_robot_end_cell = self._m_cells.get(a_col,a_row)

    def getRobotEndCell(self):
        return self._m_robot_end_cell
    