from PyPathUI.cellUI import CellMatrixUI
from PyPath.PyPath.robot import Robot

class RobotUI:
    """
    """

    def __init__(self, a_robot: Robot, a_cell_matrix_ui: CellMatrixUI, a_r: int = 0):
        """
        """
        self._m_r = a_r
        self._m_cell_matrix_ui = a_cell_matrix_ui
        self._m_robot = a_robot

        self._m_x, self._m_y = self._m_robot.getPosition()
        self._m_oval = self._m_cell_matrix_ui.create_oval(self._m_x, self._m_y, self._m_x+(self._m_r*2), self._m_y+(self._m_r*2))
        self._m_cell_matrix_ui.itemconfig(self._m_oval, fill='blue')

        self._m_robot.attach(self)

    def move(self, a_new_x: int = 0, a_new_y: int = 0):
        # Compute move
        l_d_x = ( a_new_x - self._m_x ) * self._m_cell_matrix_ui.cellWidth
        l_d_y = ( a_new_y - self._m_y ) * self._m_cell_matrix_ui.cellHeight
        
        self._m_cell_matrix_ui.move(self._m_oval, l_d_x, l_d_y)
        
        # Save new position
        self._m_x = a_new_x
        self._m_y = a_new_y

    def getPosition(self):
        return self._m_robot.getPosition()
    
    def getDestination(self):
        return self._m_robot.getDestination()
    
    def update(self):
        l_new_x, l_new_y = self._m_robot.getPosition()

        self.move(l_new_x, l_new_y)