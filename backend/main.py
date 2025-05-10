from typing import Union
from fastapi import FastAPI, Body
from warehouse_system.grid import Grid, ClassType
from warehouse_system.robot import Robot
from warehouse_system.task import Task
from warehouse_system.schedule import Scheduler
from pydantic import BaseModel

app = FastAPI()
grid = None  # Initialize grid as None here to allow use of same grid for all methods
tasks = []
robots = []

@app.get("/api/init")
def init_grid(width: int = 5, height: int = 5):
    global grid
    grid = Grid(width, height)
    return {"grid": grid.serialize()}

class Robot_Params(BaseModel):
    robot_id: str
    robot_type: str
    shift: str

class Add_Robot_Request(BaseModel):
    robots: list[Robot_Params] # list to allow multiple robots to be initialized at once

@app.post("/api/init/robot")
def add_robot(request: Add_Robot_Request = Body(...)):
    global grid
    global robots
    if grid is None:
        return {"grid_error": "Grid has not been initialized"}

    for robot_param in request.robots:
        robot = Robot(robot_param.robot_id, robot_param.robot_type, robot_param.shift)
        x, y = robot.current_position
        if grid.get_cell(x, y) != 0:
            return {"cell_error": f"Robot already exists at position {robot.current_position}"}
        grid.set_cell(x, y, robot)
        robots.append(robot)

    return {"robots": [robot.serialize() for robot in robots], "grid": grid.serialize()}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.get("/api/view")
def view_current_state():
    global grid
    if grid is None:
        return {"grid_error": "Grid has not been initialized"}
    return {"grid": grid.serialize(), "tasks": [task.serialize() for task in tasks]}

# Create running methods

class Task_Params(BaseModel):
    task_id: str
    task_type: str
    task_shift: str
    task_pickup_location: tuple[int, int]
    task_dropoff_location: tuple[int, int]

class Init_Task_Request(BaseModel):
    tasks: list[Task_Params]

@app.post("/api/init/task")
def init_task(request: Init_Task_Request = Body(...)):
    global grid
    global tasks
    if grid is None:
        return {"grid_error": "Grid has not been initialized"}
    
    for task in request.tasks:
        task = Task(int(task.task_id), task.task_type, task.task_shift, task.task_pickup_location, task.task_dropoff_location)
        tasks.append(task)
    return {"task": task.serialize() for task in tasks}

@app.get("/api/run")
def run_scheduler():
    global grid
    global tasks
    global robots
    if grid is None:
        return {"grid_error": "Grid has not been initialized"}
    
    scheduler = Scheduler(grid, tasks, robots)
    return {"scheduler": scheduler.serialize()}


@app.get("/")
async def read_root():
    return {"message": "Test"}
