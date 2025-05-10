from grid import Grid
class Robot:
    def __init__(self, grid: Grid, robot_id: str, robot_type: str, shift: str, battery_level: int = 100, current_position: tuple = (0, 0)):
        self.grid = grid
        self.robot_id = robot_id
        self.robot_type = robot_type
        self.shift = shift
        self.battery_level = battery_level
        self.is_carrying_box = False
        self.current_position = current_position

    def charge(self):
        self.battery_level = 100
        self.is_moving = False
        
        

