from tkinter import Canvas

class RobotUI:
    """
    """

    def __init__(self, canvas: Canvas, a_x: int = 0, a_y: int = 0, a_r: int = 0):
        """
        """
        self._m_x = a_x
        self._m_y = a_y
        self._m_r = a_r
        self._m_canvas = canvas

        self._m_ovale = self._m_canvas.create_oval(self._m_x-self._m_r, self._m_y-self._m_r, self._m_x+self._m_r, self._m_y+self._m_r)
        self._m_canvas.itemconfig(self._m_ovale, fill='blue')

    def move(self, a_new_x: int = 0, a_new_y: int = 0):
        # Compute move
        l_d_x = a_new_x - self._m_x
        l_d_y = a_new_y - self._m_y
        
        self._m_canvas.move(self._m_ovale, l_d_x, l_d_y)
        
        # Save new position
        self._m_x = a_new_x
        self._m_y = a_new_y