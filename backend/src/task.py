from typing import Tuple

class Task:
    def __init__(self, goal: Tuple[int, int]):
        self.__goal = goal

    def is_completed(self, position: Tuple[int, int]):
        return position == self.__goal
    
    @classmethod
    def deserialize(cls, data: dict):
        return cls(tuple(data["goal"]))

    def serialize(self):
        return {
            "goal": list(self.__goal)
        }
    
    def __str__(self):
        return f"Task(goal={self.__goal})"
    
    def __repr__(self):
        return self.__str__()
