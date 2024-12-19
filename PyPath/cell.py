class Cell:
    """
    """

    def __init__(self, a_col:int, a_row:int):
        """
        """
        self._m_col = a_col
        self._m_row = a_row

        self._m_occcupied = False
        self._m_observers = []

    def __str__(self):
        return "[%d;%d]" %(self._m_col, self._m_row)

    @property
    def row(self):
        return self._m_row
    
    @property
    def col(self):
        return self._m_col

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

class CellMatrix():
    def __init__(self, a_nb_cols:int, a_nb_rows:int):
        self._m_cells = {}

        self._m_max_col_index = a_nb_cols;
        self._m_max_row_index = a_nb_rows;

        for l_col_index in range(0, self._m_max_col_index+1):
            for l_row_index in range(0, self._m_max_row_index+1):
                self._m_cells.setdefault(l_col_index, {})[l_row_index] = Cell(l_col_index, l_row_index)


    @property
    def max_col_index(self):
        return self._m_max_col_index

    @property
    def max_row_index(self):
        return self._m_max_row_index
    
    def neighbors(self, a_col_index: int, a_row_index: int):
        l_neighbors = []

        if a_col_index == 0:
            # First col
            if a_row_index == 0:
                # First row
                l_neighbors.append((1, 0))
                # l_neighbors.append((1, 1))
                l_neighbors.append((0, 1))
            elif a_row_index == self._m_max_row_index:
                # Last row
                l_neighbors.append((1, self._m_max_row_index))
                # l_neighbors.append((1, self._m_max_row_index-1))
                l_neighbors.append((0, self._m_max_row_index-1))
            else:
                l_neighbors.append((0, a_row_index-1))
                # l_neighbors.append((1, a_row_index-1))
                l_neighbors.append((1, a_row_index))
                # l_neighbors.append((1, a_row_index+1))
                l_neighbors.append((0, a_row_index+1))
        elif a_col_index == self._m_max_col_index:
            # Last col
            if a_row_index == 0:
                # First row
                l_neighbors.append((self._m_max_col_index-1, 0))
                # l_neighbors.append((self._m_max_col_index-1, 1))
                l_neighbors.append((self._m_max_col_index, 1))
            elif a_row_index == self._m_max_row_index:
                # Last row
                l_neighbors.append((self._m_max_col_index-1, self._m_max_row_index))
                # l_neighbors.append((self._m_max_col_index-1, self._m_max_row_index-1))
                l_neighbors.append((self._m_max_col_index, self._m_max_row_index-1))
            else:
                l_neighbors.append((self._m_max_col_index, a_row_index-1))
                # l_neighbors.append((self._m_max_col_index-1, a_row_index-1))
                l_neighbors.append((self._m_max_col_index-1, a_row_index))
                # l_neighbors.append((self._m_max_col_index-1, a_row_index+1))
                l_neighbors.append((self._m_max_col_index, a_row_index+1))
        else:
            if a_row_index == 0:
                # First row
                l_neighbors.append((a_col_index-1, 0))
                # l_neighbors.append((a_col_index-1, 1))
                l_neighbors.append((a_col_index, 1))
                # l_neighbors.append((a_col_index+1, 1))
                l_neighbors.append((a_col_index+1, 0))
            elif a_row_index == self._m_max_row_index:
                # Last row
                l_neighbors.append((a_col_index-1, self._m_max_row_index))
                # l_neighbors.append((a_col_index-1, self._m_max_row_index-1))
                l_neighbors.append((a_col_index, self._m_max_row_index-1))
                # l_neighbors.append((a_col_index+1, self._m_max_row_index-1))
                l_neighbors.append((a_col_index+1, self._m_max_row_index))
            else:
                l_neighbors.append((a_col_index, a_row_index-1))
                # l_neighbors.append((a_col_index+1, a_row_index-1))
                l_neighbors.append((a_col_index+1, a_row_index))
                # l_neighbors.append((a_col_index+1, a_row_index+1))
                l_neighbors.append((a_col_index, a_row_index+1))
                # l_neighbors.append((a_col_index-1, a_row_index+1))
                l_neighbors.append((a_col_index-1, a_row_index))
                # l_neighbors.append((a_col_index-1, a_row_index-1))

        return l_neighbors

    def get(self, a_x:int, a_y:int):
        return self._m_cells[a_x][a_y]