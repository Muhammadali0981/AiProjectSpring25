from grid import Grid, ClassType
from path_finder import PathFinder

def create_test_grid() -> Grid:
    # Create a 10x10 grid
    grid = Grid(10, 10)
    
    # Add two charging stations
    grid.set_cell(2, 8, ClassType.CHARGING_STATION)  # Bottom left area
    grid.set_cell(8, 2, ClassType.CHARGING_STATION)  # Top right area
    
    # Add three obstacles in strategic positions
    grid.set_cell(3, 3, ClassType.OBSTACLE)
    grid.set_cell(5, 5, ClassType.OBSTACLE)
    grid.set_cell(7, 7, ClassType.OBSTACLE)
    
    # Add four boxes
    grid.set_cell(1, 0, ClassType.BOX)
    grid.set_cell(1, 1, ClassType.BOX)
    grid.set_cell(4, 6, ClassType.BOX)
    grid.set_cell(6, 4, ClassType.BOX)
    grid.set_cell(8, 8, ClassType.BOX)
    
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
            elif cell == ClassType.BOX:
                print("B ", end="")  # Box
            elif cell == ClassType.CHARGING_STATION:
                print("C ", end="")  # Charging Station
            else:
                print(". ", end="")  # Empty
        print()

if __name__ == "__main__":
    grid = create_test_grid()
    path_finder = PathFinder(grid)
    
    print("Initial Grid:")
    print_grid(grid)
    
    # Test path from (0,0) to first charging station at (2,8)
    start = (0, 0)
    goal = (8, 2)   # Going to the bottom-left charging station
    
    print(f"\nFinding path from {start} to charging station at {goal}")
    path = path_finder.find_path(start, goal)
    
    if path:
        print("\nPath found! Here's the grid with the path marked (*):")
        print_grid(grid, path)
        print(f"\nPath length: {len(path)} steps")
    else:
        print("\nNo path found!")