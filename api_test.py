import requests
import json

grid = {}
tasks = []
robots = []
def test_create_warehouse():
    global grid
    response = requests.post("http://localhost:8000/api/init", json={"width": 4, "height": 4})
    assert response.status_code == 200
    grid = response.json()["grid"]
    print(json.dumps(grid, indent=4))

def test_add_robot():
    global grid
    global robots
    response = requests.post("http://localhost:8000/api/init/robot", json={
        "robots": [{ "robot_id": "robot1", "robot_type": "picker", "shift": "day", "current_position": [0, 0] }],
        "grid": grid
    })
    assert response.status_code == 200
    grid = response.json()["grid"]
    robots = response.json()["robots"]
    print(json.dumps(grid, indent=4))
    print(json.dumps(robots, indent=4))

def test_run_warehouse():
    global grid, tasks, robots

    response = requests.post("http://localhost:8000/api/run", json={
        "grid": grid,
        "tasks": [{"task_id": "1", "task_type": "pickup", "task_shift": "day", "task_pickup_location": [0, 0], "task_dropoff_location": [3, 3]}],
        "robots": robots
    })
    assert response.status_code == 200
    scheduler = response.json()["scheduler"]
    print(json.dumps(scheduler, indent=4))

if __name__ == "__main__":
    test_create_warehouse()
    test_add_robot()
    test_run_warehouse()