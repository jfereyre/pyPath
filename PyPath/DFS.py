from PyPathUI.cellUI import CellUI

def det(a_vec1: tuple , a_neighbor: tuple, a_end: CellUI):

    l_vec2 = (a_end.row - a_neighbor[1], a_end.col - a_neighbor[0] )

    return ( a_vec1[0] * l_vec2[1] )- ( a_vec1[1] * l_vec2[0] )
      

def DFS(a_start : CellUI, a_end: CellUI, a_cells: dict):
    """
    """
    a_start.visit()

    l_start_vec = (a_end.row-a_start.row, a_end.col - a_start.col)

    if a_start.row == a_end.row and a_start.col == a_end.col:
        print("FOUND!!!!")
        return [a_start]

    l_sorted_neighbors =  sorted(a_start.neighbors, key=lambda neighbor: det(l_start_vec, neighbor, a_end))
    
    for l_next_path in l_sorted_neighbors:

            l_next_path_col, l_next_path_row = l_next_path

            l_cell = a_cells[l_next_path_col][l_next_path_row]

            if not l_cell.visited and not l_cell.isOccupied():
                    
                    l_full_path = DFS(l_cell, a_end, a_cells)

                    if isinstance(l_full_path, list):
                        l_full_path.insert(0, a_start)
                        return l_full_path

    a_start.setColor('black')               
                
    return None

