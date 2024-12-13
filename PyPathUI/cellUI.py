from PyPath.cell import Cell, CellMatrix
from tkinter import Canvas

class CellMatrixUI(Canvas):
    
    def __init__(self, a_cell_matrix: CellMatrix, a_parent, a_width: int, a_height: int):
        """
        """
        super().__init__(a_parent, width=a_width, height=a_height)

        self._m_cell_matrix = a_cell_matrix
        self._m_cells_ui = {}

        for l_cell_col in range(0, self._m_cell_matrix.max_col_index):
            for l_cell_row in range(0, self._m_cell_matrix.max_row_index):
                self._m_cells_ui.setdefault(l_cell_col, {})[l_cell_row] = CellUI(self, self._m_cell_matrix.get(l_cell_col, l_cell_row))

    @property
    def cellHeight(self):
        return int(self['height']) // self._m_cell_matrix.max_row_index
    
    @property
    def cellWidth(self):
        return int(self['width']) // self._m_cell_matrix.max_col_index

    def get(self, a_col:int, a_row: int):
        return self._m_cells_ui[a_col][a_row]

class CellUI(object):
    """
    """
    def __init__(self, a_cell_matrix_ui: CellMatrixUI, a_cell: Cell):
        """
        """
        self._m_cell_matrix_ui = a_cell_matrix_ui
 
        self._m_cell = a_cell

        self._m_rectangle = self._m_cell_matrix_ui.create_rectangle(self._m_cell.col * self._m_cell_matrix_ui.cellHeight,
                                                            self._m_cell.row * self._m_cell_matrix_ui.cellWidth,
                                                            (self._m_cell.col + 1) * self._m_cell_matrix_ui.cellHeight,
                                                            (self._m_cell.row + 1) * self._m_cell_matrix_ui.cellWidth,
                                                            fill='white')

        self._m_cell.attach(self)

    @property
    def row(self):
        return self._m_cell.row
    
    @property
    def col(self):
        return self._m_cell.col

    def __str__(self):
        l_message = "[%d,%d]"  % (self.col, self.row)
        return l_message

    def update(self, l_cell):
        """
        """
        if self._m_cell.isOccupied():
            self._m_cell_matrix_ui.itemconfig(self._m_rectangle, fill='red')
        else:
            self._m_cell_matrix_ui.itemconfig(self._m_rectangle, fill='white')

    def setColor(self, a_color: str):
        self._m_cell_matrix_ui.itemconfig(self._m_rectangle, fill=a_color)


