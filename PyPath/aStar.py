from PyPath.cell import CellMatrix
import heapq

class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g  # Coût pour atteindre ce nœud depuis le départ
        self.h = h  # Heuristique : estimation du coût pour aller jusqu'à l'arrivée
        self.f = g + h  # Coût total estimé

    def __lt__(self, other):
        return self.f < other.f

class Algo:
    def __init__(self, a_cells: CellMatrix, a_max_col_index:int, a_max_row_index: int):
        self._m_cells = a_cells
        self._m_max_col_index = a_max_col_index
        self._m_max_row_index = a_max_row_index

    def run(self, start, goal):
        open_set = []
        closed_set = set()
        heapq.heappush(open_set, Node(start, None, 0, Algo.heuristic(start, goal)))
        
        while open_set:
            current = heapq.heappop(open_set)
            
            if current.state == goal:
                path = []
                while current:
                    path.append(current.state)
                    current = current.parent
                return path[::-1]
            
            closed_set.add(current.state)
            for neighbor in self.neighbors(current.state):
                if self._m_cells.get(neighbor[0],neighbor[1]).isOccupied():
                    continue
                if neighbor in closed_set:
                    continue
                tentative_g = current.g + 1  # Coût pour aller du nœud courant au voisin
                tentative_node = Node(neighbor, current, tentative_g, Algo.heuristic(neighbor, goal))
                if tentative_node not in open_set:
                    heapq.heappush(open_set, tentative_node)
                elif tentative_g < tentative_node.g:
                    open_set.remove(tentative_node)
                    heapq.heapush(open_set, tentative_node)
        
        return None  # Pas de chemin trouvé

    def neighbors(self, state):
        # Cette fonction doit retourner les voisins d'un état donné
        # Par exemple, pour une grille :
        x, y = state
        return self._m_cells.neighbors(x,y)


    @staticmethod
    def heuristic(a, b):
        # Heuristique de la distance de Manhattan (exemple)
        x1, y1 = a
        x2, y2 = b
        return abs(x1 - x2) + abs(y1 - y2)


def AStar(a_start:tuple, a_end: tuple, a_cells: CellMatrix):
    l_astar = Algo(a_cells, a_cells.max_col_index-1, a_cells.max_row_index-1)

    # Trouver le chemin du point (0, 0) au point (3, 3) sur une grille
    path = l_astar.run(a_start, a_end)
 
    l_path_cells = []
    if not path == None:
        for l_path in path:
            l_path_cells.append(a_cells.get(l_path[0],l_path[1]))

    return l_path_cells