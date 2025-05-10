from grid import Grid, ClassType
from robot import Robot
import heapq

class PathFinder:
    def __init__(self, grid: Grid):
        self.grid = grid
    
    def heuristic(self, a: tuple, b: tuple) -> float:
        """Manhattan distance heuristic"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def get_tile_cost(self, position: tuple, carrying_box: bool) -> float:
        r, c = position
        tile_type = self.grid.get_cell(c, r)
        
        base_costs = {
            ClassType.EMPTY: 1,
            ClassType.RAMP: 2,
            ClassType.SLOPE: 3,
            ClassType.CHARGING_STATION: 1,
        }
        
        cost = base_costs.get(tile_type, float('inf'))
        
        if carrying_box:
            cost *= 2
    
        return cost


    def find_path(self, robot: Robot, goal: tuple) -> list:
        """A* search algorithm to find the shortest path considering movement rules."""
        self.grid.convert_to_adjacency_list()
        adjacency_list = self.grid.get_adjacency_list()

        pq = []
        heapq.heappush(pq, (self.heuristic(robot.current_position, goal), robot.current_position))

        g_score = {robot.current_position: 0}
        parent = {robot.current_position: None}

        while pq:
            _, node = heapq.heappop(pq)

            if node == goal:
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return list(reversed(path))

            for neighbor in adjacency_list.get(node, []):
                new_g = g_score[node] + self.get_tile_cost(neighbor, robot.is_carrying_box)

                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    f_score = new_g + self.heuristic(neighbor, goal)
                    heapq.heappush(pq, (f_score, neighbor))
                    parent[neighbor] = node

        return None

    def compute_battery_cost(self, path: list, carrying: bool) -> int:
        if not path:
            return float('inf')
        return int(len(path) * (2 if carrying else 1))
