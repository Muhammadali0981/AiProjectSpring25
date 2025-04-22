import requests
import json

warehouse = {}

def test_create_warehouse():
    global warehouse

    response = requests.get("http://localhost:8000/warehouse?x=4&y=4")
    assert response.status_code == 200
    warehouse = response.json()["warehouse"]
    print(json.dumps(warehouse, indent=4))

def test_add_robot():
    global warehouse

    response = requests.post("http://localhost:8000/warehouse/robot", json={
        "robots": [{ "name": "robot1", "position": [0, 0] }],
        "warehouse": warehouse
    })
    assert response.status_code == 200
    warehouse = response.json()["warehouse"]
    print(json.dumps(warehouse, indent=4))

def test_set_robot_task():
    global warehouse

    response = requests.post("http://localhost:8000/warehouse/robot/robot1", json={
        "task": { "goal": [3, 3] },
        "warehouse": warehouse
    })
    assert response.status_code == 200
    warehouse = response.json()["warehouse"]
    print(json.dumps(warehouse, indent=4))

def test_run_warehouse():
    global warehouse

    response = requests.get("http://localhost:8000/warehouse/run", json={
        "warehouse": warehouse
    })
    assert response.status_code == 200
    warehouse = response.json()["warehouse"]
    print(json.dumps(warehouse, indent=4))
    distances = response.json()["distances"]

    print("Distances:")
    print(json.dumps(distances, indent=4))

if __name__ == "__main__":
    test_create_warehouse()
    test_add_robot()
    test_set_robot_task()
    test_run_warehouse()
