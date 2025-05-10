from schedule import Scheduler
from grid import Grid, ClassType
from robot import Robot
from task import Task

def simulate_basic_direct():
    grid = Grid(5, 5)
    tasks = [Task(1, 'standard', 'day', (1, 1), (3, 3))]
    robots = [Robot('R1', 'standard', 'day', current_position=(0, 0))]

    scheduler = Scheduler(grid, tasks, robots)

    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_low_battery_charge_needed():
    grid = Grid(6, 6)
    grid.set_cell(0, 0, ClassType.CHARGING_STATION)

    tasks = [Task(1, 'fragile', 'day', (2, 2), (3, 3))]
    robots = [Robot('R1', 'fragile', 'day', battery_level=3, current_position=(1, 1))]

    scheduler = Scheduler(grid, tasks, robots)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_path_blocked():
    grid = Grid(5, 5)
    for i in range(5):
        grid.set_cell(2, i, ClassType.OBSTACLE)  # vertical wall
    grid.set_cell(2, 2, ClassType.EMPTY)

    tasks = [Task(1, 'standard', 'day', (3, 3), (6, 6))]
    robots = [Robot('R1', 'standard', 'day', current_position=(0, 0))]

    scheduler = Scheduler(grid, tasks, robots)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_robot_competition():
    grid = Grid(7, 7)
    tasks = [Task(1, 'standard', 'day', (1, 1), (6, 6))]

    robots = [
        Robot('R1', 'standard', 'day', battery_level=100, current_position=(6, 6)),
        Robot('R2', 'standard', 'day', battery_level=100, current_position=(0, 0)),
    ]

    scheduler = Scheduler(grid, tasks, robots)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_task_overload():
    grid = Grid(6, 6)

    tasks = [
        Task(1, 'fragile', 'day', (1, 1), (2, 2)),
        Task(2, 'fragile', 'day', (3, 3), (4, 4)),
        Task(3, 'fragile', 'day', (0, 5), (5, 0))
    ]

    robots = [
        Robot('R1', 'fragile', 'day', current_position=(0, 0)),
        Robot('R2', 'fragile', 'day', current_position=(5, 5))
    ]

    scheduler = Scheduler(grid, tasks, robots)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_type_or_shift_mismatch():
    grid = Grid(5, 5)

    tasks = [Task(1, 'heavy', 'night', (0, 0), (1, 1))]
    robots = [Robot('R1', 'standard', 'day', current_position=(0, 0))]

    scheduler = Scheduler(grid, tasks, robots)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def test_deserialize():
    grid = Grid(5, 5)
    grid.set_cell(0, 0, ClassType.OBSTACLE)
    serialized = grid.serialize()
    new_grid = Grid.deserialize(serialized)
    assert new_grid.get_cell(0, 0) == ClassType.OBSTACLE

def run_all_tests():
    print("\n========== TEST: Basic Direct Assignment ==========")
    simulate_basic_direct()

    print("\n========== TEST: Low Battery Needs Charging ==========")
    simulate_low_battery_charge_needed()

    print("\n========== TEST: Path Blocked by Obstacles ==========")
    simulate_path_blocked()

    print("\n========== TEST: Robot Competition for Task ==========")
    simulate_robot_competition()

    print("\n========== TEST: Too Many Tasks for Robots ==========")
    simulate_task_overload()

    print("\n========== TEST: Type/Shift Incompatibility ==========")
    simulate_type_or_shift_mismatch()

    print("\n========== TEST: Serialization/Deserialization ==========")
    test_deserialize()

if __name__ == "__main__":
    run_all_tests()
