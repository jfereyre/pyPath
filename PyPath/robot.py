from PyPath.aStar import AStar
from PyPath.cell import CellMatrix

class RobotNoMoreMoveException(Exception):
    def __init__(self):
        super().__init__()

class Robot(object):
    def __init__(self):
        """
        """
        self._m_col = 0
        self._m_row = 0
        self._m_start_col = 0
        self._m_start_row = 0
        self._m_destination_col = 0
        self._m_destination_row = 0
        self._m_path = []
        self._m_observers = []

    def setPosition(self, a_col:int, a_row:int):
        """
        """
        self._m_col = a_col
        self._m_row = a_row

    def setDestination(self, a_col:int, a_row:int):
        """
        """
        self._m_destination_col = a_col
        self._m_destination_row = a_row

    def setStartPosition(self, a_col:int, a_row:int):
        """
        """
        self._m_start_col = a_col
        self._m_start_row = a_row
        self.setPosition(a_col, a_row)

    def getPosition(self):
        """
        """
        return (self._m_col, self._m_row)

    def getDestination(self):
        """
        """
        return (self._m_destination_col, self._m_destination_row)

    def getStartPosition(self):
        """
        """
        return (self._m_start_col, self._m_start_row)

    def buildPath(self, a_cells: CellMatrix):
        """
        """
        self._m_path = AStar((self._m_col, self._m_row), (self._m_destination_col, self._m_destination_row), a_cells)[1:]

    def move(self, a_cells: CellMatrix):
        """
        """
        self.buildPath(a_cells)

        if self._m_path:
            l_next_position = self._m_path.pop(0)
            self._m_col = l_next_position.col
            self._m_row = l_next_position.row
            self.notify()
        else:
            raise RobotNoMoreMoveException()
    
    def attach(self, a_observer):
        """
        """
        self._m_observers.append(a_observer)
    
    def detach(self, a_observer):
        """
        """
        self._m_observers.remove(a_observer)

    def notify(self):
        """
        """
        for l_observer in self._m_observers:
            l_observer.update()
