from grid import Grid
class Robot:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.is_moving = False
        self.battery_level = 100
        self.is_carrying_box = False
        self.current_position = (0, 0)
        self.path = []

    def charge(self):
        self.battery_level = 100
        self.is_moving = False
        
        

