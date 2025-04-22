from typing import Tuple, List
from src.cell import CellType

class Grid:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__grid: List[List[CellType]] = [[CellType.EMPTY for _ in range(width)] for _ in range(height)]

    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_cell(self, x: int, y: int) -> CellType:
        return self.__grid[x][y]
    
    def set_cell(self, x: int, y: int, value: CellType):
        self.__grid[x][y] = value
    
    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = []
        # do not allow diagonal movement
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy:
                    continue
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.__width and 0 <= ny < self.__height and self.__grid[nx][ny] != CellType.OBSTACLE:
                    neighbors.append((nx, ny))
        return neighbors

    def serialize(self):
        return {
            "width": self.__width,
            "height": self.__height,
            "cells": [str(cell) for row in self.__grid for cell in row]
        }

    @classmethod
    def deserialize(cls, data: dict):
        grid = cls(data["width"], data["height"])
        for i in range(data["width"]):
            for j in range(data["height"]):
                grid.set_cell(i, j, CellType.from_string(data["cells"][i * data["height"] + j]))
        return grid

    def __str__(self):
        return f"Grid(width={self.__width}, height={self.__height}, grid={self.__grid})"
    
    def __repr__(self):
        return self.__str__()
