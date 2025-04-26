from grid import Grid, ClassType
from path_finder import PathFinder
from robot import Robot

def create_test_grid() -> Grid:
    # Create a 10x10 grid
    grid = Grid(10, 10)
    
    # Add charging stations
    grid.set_cell(2, 8, ClassType.CHARGING_STATION)  # Bottom left area
    grid.set_cell(8, 2, ClassType.CHARGING_STATION)  # Top right area
    
    # Add some ramps and slopes to test battery consumption
    grid.set_cell(3, 3, ClassType.RAMP)
    grid.set_cell(5, 5, ClassType.OBSTACLE)
    grid.set_cell(4, 4, ClassType.RAMP)
    
    # Add obstacles to make path planning interesting
    grid.set_cell(6, 1, ClassType.OBSTACLE)
    grid.set_cell(6, 2, ClassType.OBSTACLE)
    grid.set_cell(2, 7, ClassType.OBSTACLE)
    grid.set_cell(6, 3, ClassType.OBSTACLE)
    grid.set_cell(1, 6, ClassType.OBSTACLE)
    grid.set_cell(4, 6, ClassType.OBSTACLE)
    grid.set_cell(2, 9, ClassType.OBSTACLE)
    grid.set_cell(6, 4, ClassType.OBSTACLE)
    grid.set_cell(2, 6, ClassType.OBSTACLE)
    grid.set_cell(3, 6, ClassType.OBSTACLE)
    
    # Initialize adjacency list
    grid.convert_to_adjacency_list()
    
    return grid

def print_grid(grid: Grid, path: list = None):
    """Print the grid with optional path visualization"""
    if path is None:
        path = []
    
    # Print column numbers
    print("  ", end="")
    for x in range(grid.get_width()):
        print(f"{x} ", end="")
    print()
    
    for y in range(grid.get_height()):
        print(f"{y} ", end="")
        for x in range(grid.get_width()):
            cell = grid.get_cell(x, y)
            if (y, x) in path:
                print("* ", end="")  # Path
            elif cell == ClassType.OBSTACLE:
                print("# ", end="")  # Wall
            elif cell == ClassType.CHARGING_STATION:
                print("C ", end="")  # Charging Station
            elif cell == ClassType.RAMP:
                print("R ", end="")  # Ramp
            elif cell == ClassType.SLOPE:
                print("S ", end="")  # Slope
            elif cell == ClassType.ROBOT:
                print("@ ", end="")  # Robot
            else:
                print(". ", end="")  # Empty
        print()

if __name__ == "__main__":
    # Create the grid
    grid = create_test_grid()
    
    # Create a robot at position (0,0) with 100 battery
    robot = Robot(grid)
    robot.current_position = (0, 0)
    robot.battery_level = 100
    
    # Create path finder
    path_finder = PathFinder(grid)
    
    print("Initial Grid (@ = Robot, C = Charging Station, R = Ramp, S = Slope):")
    print_grid(grid)
    
    # Test path from robot's position to charging station at (8,2)
    goal = (8, 3)  # Top-right charging station
    
    print(f"\nFinding path from Robot at {robot.current_position} to charging station at {goal}")
    print(f"Initial battery level: {robot.battery_level}")
    
    path = path_finder.find_path(robot, goal)
    
    if path:
        print("\nPath found! Here's the grid with the path marked (*):")
        print_grid(grid, path)
        print(f"\nPath length: {len(path)} steps")
    else:
        print("\nNo path found!")