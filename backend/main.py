from typing import Union, Optional
from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from warehouse_system.grid import Grid, ClassType
from warehouse_system.robot import Robot
from warehouse_system.task import Task
from warehouse_system.schedule import Scheduler
from pydantic import BaseModel

app = FastAPI()

class Grid_Request(BaseModel):
    width: int = 5
    height: int = 5

@app.post("/api/init")
def init_grid(request: Grid_Request):
    grid = Grid(request.width, request.height)
    return {"grid": grid.serialize()}

class Robot_Params(BaseModel):
    robot_id: str
    robot_type: str
    shift: str
    current_position: tuple[int, int]

class Add_Robot_Request(BaseModel):
    grid: Union[dict, None] = None
    robots: list[Robot_Params] # list to allow multiple robots to be initialized at once

@app.post("/api/init/robot")
def add_robot(request: Add_Robot_Request):
    if request.grid is None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"grid_error": "Grid has not been initialized"})
    grid = Grid.deserialize(request.grid)
    robots = []
    for robot_param in request.robots:
        robot = Robot(robot_param.robot_id, robot_param.robot_type, robot_param.shift, current_position=robot_param.current_position)
        x, y = robot.current_position
        if grid.get_cell(x, y) != 0:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"cell_error": f"Robot already exists at position {robot.current_position}"})
        grid.set_cell(x, y, ClassType.ROBOT)
        robots.append(robot)

    return {"grid": grid.serialize(), "robots": [robot.serialize() for robot in robots]}

# @app.get("/api/view")
# def view_current_state(state: State = Depends(get_state)):
#     if state.grid is None:
#         return {"grid_error": "Grid has not been initialized"}
#     return {"grid": state.grid.serialize(), "tasks": [task.serialize() for task in state.tasks]}

# # Create running methods

class Task_Params(BaseModel):
    task_id: str
    task_type: str
    task_shift: str
    task_pickup_location: tuple[int, int]
    task_dropoff_location: tuple[int, int]

class Run_Scheduler_Request(BaseModel):
    grid: Union[dict, None] = None
    tasks: list[Task_Params]
    robots: list[dict, None] = None

@app.post("/api/run")
def run_scheduler(request: Run_Scheduler_Request):
    if request.grid is None or request.tasks is None or request.robots is None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"general_error": "Missing required fields"})
    grid = Grid.deserialize(request.grid)
    tasks = []
    robots = [Robot.deserialize(robot) for robot in request.robots]
    for task in request.tasks:
        task = Task(int(task.task_id), task.task_type, task.task_shift, task.task_pickup_location, task.task_dropoff_location)
        tasks.append(task)
    scheduler = Scheduler(grid, tasks, robots)
    print(scheduler.serialize())
    return {"scheduler": scheduler.serialize()}


# @app.get("/")
# async def read_root():
#     return {"message": "Test"}
