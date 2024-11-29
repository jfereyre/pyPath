from PyPath.cell import Cell
from tkinter import Canvas

class CellUI(Cell):
    """
    """
    def __init__(self, canvas: Canvas, a_col_index:int = 0 , a_row_index: int = 0, a_cell_width: int = 0, a_cell_height: int = 0, a_max_col_index: int = 0, a_max_row_index: int = 0):
        """
        """
        super().__init__(a_col_index * a_cell_width, a_row_index * a_cell_height, (a_col_index + 1) * a_cell_width, (a_row_index + 1) * a_cell_height)
        
        self._m_row_index = a_row_index
        self._m_col_index = a_col_index

        self._m_canvas = canvas
        self._m_rectangle = self._m_canvas.create_rectangle(self._m_x_0, self._m_y_0, self._m_x_1, self._m_y_1, fill='white')

        self.build_neighborhood(a_max_col_index, a_max_row_index)

        self.attach(self)

    @property
    def row(self):
        return self._m_row_index
    
    @property
    def col(self):
        return self._m_col_index

    def __str__(self):
        l_message = "[%d,%d]"  % (self._m_col_index, self._m_row_index)
        l_message += " - visited " + str(self.visited)
        return l_message

    def update(self, l_cell):
        """
        """
        if self.isOccupied():
            self._m_canvas.itemconfig(self._m_rectangle, fill='red')
        else:
            self._m_canvas.itemconfig(self._m_rectangle, fill='white')

    def setColor(self, a_color: str):
        self._m_canvas.itemconfig(self._m_rectangle, fill=a_color)

    def build_neighborhood(self, a_max_col_index: int = 0, a_max_row_index: int = 0):
        self._m_neighbors = []

        if self._m_col_index == 0:
            # First col
            if self._m_row_index == 0:
                # First row
                self._m_neighbors.append((1, 0))
                # self._m_neighbors.append((1, 1))
                self._m_neighbors.append((0, 1))
            elif self._m_row_index == a_max_row_index:
                # Last row
                self._m_neighbors.append((1, a_max_row_index))
                # self._m_neighbors.append((1, a_max_row_index-1))
                self._m_neighbors.append((0, a_max_row_index-1))
            else:
                self._m_neighbors.append((0, self._m_row_index-1))
                # self._m_neighbors.append((1, self._m_row_index-1))
                self._m_neighbors.append((1, self._m_row_index))
                # self._m_neighbors.append((1, self._m_row_index+1))
                self._m_neighbors.append((0, self._m_row_index+1))
        elif self._m_col_index == a_max_col_index:
            # Last col
            if self._m_row_index == 0:
                # First row
                self._m_neighbors.append((a_max_col_index-1, 0))
                # self._m_neighbors.append((a_max_col_index-1, 1))
                self._m_neighbors.append((a_max_col_index, 1))
            elif self._m_row_index == a_max_row_index:
                # Last row
                self._m_neighbors.append((a_max_col_index-1, a_max_row_index))
                # self._m_neighbors.append((a_max_col_index-1, a_max_row_index-1))
                self._m_neighbors.append((a_max_col_index, a_max_row_index-1))
            else:
                self._m_neighbors.append((a_max_col_index, self._m_row_index-1))
                # self._m_neighbors.append((a_max_col_index-1, self._m_row_index-1))
                self._m_neighbors.append((a_max_col_index-1, self._m_row_index))
                # self._m_neighbors.append((a_max_col_index-1, self._m_row_index+1))
                self._m_neighbors.append((a_max_col_index, self._m_row_index+1))
        else:
            if self._m_row_index == 0:
                # First row
                self._m_neighbors.append((self._m_col_index-1, 0))
                # self._m_neighbors.append((self._m_col_index-1, 1))
                self._m_neighbors.append((self._m_col_index, 1))
                # self._m_neighbors.append((self._m_col_index+1, 1))
                self._m_neighbors.append((self._m_col_index+1, 0))
            elif self._m_row_index == a_max_row_index:
                # Last row
                self._m_neighbors.append((self._m_col_index-1, a_max_row_index))
                # self._m_neighbors.append((self._m_col_index-1, a_max_row_index-1))
                self._m_neighbors.append((self._m_col_index, a_max_row_index-1))
                # self._m_neighbors.append((self._m_col_index+1, a_max_row_index-1))
                self._m_neighbors.append((self._m_col_index+1, a_max_row_index))
            else:
                self._m_neighbors.append((self._m_col_index, self._m_row_index-1))
                # self._m_neighbors.append((self._m_col_index+1, self._m_row_index-1))
                self._m_neighbors.append((self._m_col_index+1, self._m_row_index))
                # self._m_neighbors.append((self._m_col_index+1, self._m_row_index+1))
                self._m_neighbors.append((self._m_col_index, self._m_row_index+1))
                # self._m_neighbors.append((self._m_col_index-1, self._m_row_index+1))
                self._m_neighbors.append((self._m_col_index-1, self._m_row_index))
                # self._m_neighbors.append((self._m_col_index-1, self._m_row_index-1))

    @property
    def neighbors(self):
        return self._m_neighbors
