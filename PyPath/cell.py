from math import sqrt

class Cell:
    """
    """

    def __init__(self, a_x_0: int = 0, a_y_0: int = 0, a_x_1: int = 0, a_y_1: int = 0):
        """
        """
        self._m_x_0 = a_x_0
        self._m_y_0 = a_y_0
        self._m_x_1 = a_x_1
        self._m_y_1 = a_y_1
        self._m_occcupied = False
        self._m_observers = []

        self._m_x_center = self._m_x_0 + ( (self._m_x_1 - self._m_x_0) / 2 ) 
        self._m_y_center = self._m_y_0 + ( (self._m_y_1 - self._m_y_0) / 2 ) 

    def __str__(self):
        return "[%d;%d] - [%d;%d]" %(self._m_x_0, self._m_y_0, self._m_x_1, self._m_y_1)
    
    def isIn(self, a_x: int, a_y: int):
        return (a_x > self._m_x_0 and a_x < self._m_x_1 and a_y > self._m_y_0 and a_y < self._m_y_1)
    
    def occupied(self):
        self._m_occcupied = True
        self.notify()
    
    def free(self):
        self._m_occcupied = False
        self.notify()

    def isOccupied(self):
        return self._m_occcupied

    def attach(self, a_observer):
        self._m_observers.append(a_observer)
    
    def detach(self, a_observer):
        self._m_observers.remove(a_observer)

    def notify(self):
        for l_observer in self._m_observers:
            l_observer.update(self)
        