class ClassType:
    EMPTY = 0
    RAMP = 1
    SLOPE = 2
    OBSTACLE = 3
    ROBOT = 4
    BOX = 5
    CHARGING_STATION = 6

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[ClassType.EMPTY for _ in range(width)] for _ in range(height)]
        self.adjacency_list = {}
    
    def convert_to_adjacency_list(self):
        self.adjacency_list = {}
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] in [ClassType.EMPTY, ClassType.BOX]:  # walkable tiles
                    node = (r, c)
                    self.adjacency_list[node] = []
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.height and 0 <= nc < self.width and self.grid[nr][nc] in [ClassType.EMPTY, ClassType.BOX]:
                            self.adjacency_list[node].append((nr, nc))


    def get_cell_cost(self, x: int, y: int):
        if self.grid[y][x] == ClassType.RAMP:
            return 2
        return 1
    
    def set_cell(self, x: int, y: int, cell_type: ClassType):
        self.grid[y][x] = cell_type
    
    def get_cell(self, x: int, y: int) -> ClassType:
        return self.grid[y][x]  
    
    def get_adjacency_list(self):
        return self.adjacency_list
    
    def get_grid(self):
        return self.grid

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height


