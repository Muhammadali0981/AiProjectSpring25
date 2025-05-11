from warehouse_system.grid import Grid
from warehouse_system.robot import Robot
from warehouse_system.task import Task
from warehouse_system.schedule import Scheduler
from warehouse_system.enums import CellType

class Warehouse:
  def __init__(self, grid: Grid, robots: list[Robot] = [], tasks: list[Task] = []):
    self.grid = grid
    self.__robots = robots
    self.__tasks = tasks

  @classmethod
  def deserialize(cls, data: dict):
    if "grid" not in data:
      raise KeyError("'grid' not in data")
    if "robots" not in data:
      raise KeyError("'robots' not in data")
    if "tasks" not in data:
      raise KeyError("'tasks' not in data")
    return cls(
      Grid.deserialize(data["grid"]),
      list(map(Robot.deserialize, data["robots"])),
      list(map(Task.deserialize, data["tasks"]))
    )

  def add_robot(self, robot: Robot):
    self.__robots.append(robot)
    self.grid.set_cell(robot.current_position[0], robot.current_position[1], CellType.ROBOT)

  def add_task(self, task: Task):
    self.__tasks.append(task)

  def serialize(self):
    return {
      "grid": self.grid.serialize(),
      "robots": list(map(Robot.serialize, self.__robots)),
      "tasks": list(map(Task.serialize, self.__tasks))
    }
  
  def get_scheduler(self):
    return Scheduler(self.grid, self.__tasks, self.__robots)
