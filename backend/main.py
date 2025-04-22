from typing import Union
from src.warehouse import Warehouse
from src.robot import Robot
from src.grid import Grid
from src.task import Task

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/warehouse")
async def get_warehouse(x: int = 10, y: int = 10):
    warehouse = Warehouse(Grid(x, y))
    return {
        "message": "Warehouse created successfully",
        "warehouse": warehouse.serialize()
    }

@app.patch("/warehouse")
async def patch_warehouse(body: dict):
    warehouse = Warehouse()
    warehouse.deserialize(body["warehouse"])
    warehouse.run()

    return { "message": "Warehouse updated successfully", "warehouse": warehouse.serialize() }

@app.post("/warehouse/robot")
async def post_warehouse_robot(body: dict):
    warehouse = Warehouse.deserialize(body["warehouse"])
    for robot in body["robots"]:
        warehouse.add_robot(Robot(robot["name"], tuple(robot["position"])))
    
    return { "message": "Robot added successfully", "warehouse": warehouse.serialize() }

@app.post("/warehouse/robot/{name}")
async def post_warehouse_robot_task(name: str, body: dict):
    warehouse = Warehouse.deserialize(body["warehouse"])
    robot = warehouse.get_robot(name)
    if robot is None:
        return { "message": "Robot not found" }
    robot.set_task(Task.deserialize(body["task"]))
    return { "message": "Robot task set successfully", "warehouse": warehouse.serialize() }

@app.get("/warehouse/run")
async def get_warehouse_run(body: dict):
    warehouse = Warehouse.deserialize(body["warehouse"])
    distances = warehouse.run()
    return {
        "message": "Warehouse run successfully",
        "distances": distances,
        "warehouse": warehouse.serialize()
    }
