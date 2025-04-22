from typing import List
from src.grid import Grid
from src.cell import CellType
from src.robot import Robot

class Warehouse:
    def __init__(self, grid: Grid = Grid(10, 10)):
        self.__grid = grid
        self.__robots: List[Robot] = []
        # self._setup_grid()

    def _setup_grid(self):
        self.__grid.set_cell(0, 0, CellType.START)
        self.__grid.set_cell(self.__grid.get_width() - 1, self.__grid.get_height() - 1, CellType.END)

    def add_robot(self, robot: Robot):
        self.__robots.append(robot)

    def get_robot(self, name: str):
        return next((r for r in self.__robots if r.get_name() == name), None)

    def run(self):
        distances = {}
        for robot in self.__robots:
            distance, path = robot.complete_task(self.__grid)
            if distance != -1:
                distances[robot.get_name()] = {
                    "distance": distance,
                    "path": path
                }
        return distances

    def serialize(self):
        return {
            "grid": self.__grid.serialize(),
            "robots": [robot.serialize() for robot in self.__robots]
        }

    @classmethod
    def deserialize(cls, data: dict):
        warehouse = cls(Grid.deserialize(data["grid"]))
        warehouse.__robots = [Robot.deserialize(robot) for robot in data["robots"]]
        return warehouse

    def __str__(self):
        return f"Warehouse(grid={self.__grid}, robots={self.__robots})"
    
    def __repr__(self):
        return self.__str__()
    