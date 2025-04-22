from typing import Tuple, Optional
from src.grid import Grid
from src.task import Task
from collections import deque

class Robot:
    def __init__(self, name: str, position: Tuple[int, int] = (0, 0)):
        self.__name = name
        self.__position = position
        self.__task: Optional[Task] = None

    @classmethod
    def deserialize(cls, data: dict):
        robot = cls(data["name"], tuple(data["position"]))
        robot.__task = Task.deserialize(data["task"]) if data["task"] else None
        return robot

    def set_task(self, task: Task):
        self.__task = task

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_task(self):
        return self.__task
    
    def complete_task(self, grid: Grid):
        if self.__task is None:
            return -1
        
        fringe = deque([(self.__position, 0, [])])
        visited = set()
        while fringe:
            (x, y), distance, path = fringe.popleft()
            if self.__task.is_completed((x, y)):
                self.__position = (x, y)
                self.__task = None
                return distance, path + [(x, y)]
            visited.add((x, y))
            for neighbor in grid.get_neighbors(x, y):
                if neighbor not in visited:
                    fringe.append((neighbor, distance + 1, path + [(x, y)]))
        return -1

    def serialize(self):
        return {
            "name": self.__name,
            "position": list(self.__position),
            "task": self.__task.serialize() if self.__task else None
        }
    
    def __str__(self):
        return f"Robot(name={self.__name}, position={self.__position}, task={self.__task})"
    
    def __repr__(self):
        return self.__str__()
        