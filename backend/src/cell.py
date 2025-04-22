from enum import Enum

class CellType(Enum):
    EMPTY = 0
    OBSTACLE = 1
    ROBOT = 2
    START = 3
    END = 4

    @staticmethod
    def from_string(string: str):
        return CellType[string]

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
