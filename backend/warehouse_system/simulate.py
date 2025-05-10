from schedule import Scheduler
from grid import Grid, ClassType
from robot import Robot

def simulate_basic_direct():
    grid = Grid(5, 5)
    tasks = [{'id': 1, 'type': 'standard', 'shift': 'day'}]
    robots = [Robot(grid, 'R1', 'standard', 'day', current_position=(0, 0))]

    task_locations = {
        1: {'pickup': (1, 1), 'dropoff': (3, 3)}
    }

    scheduler = Scheduler(grid, tasks, robots, task_locations)

    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_low_battery_charge_needed():
    grid = Grid(6, 6)
    grid.set_cell(0, 0, ClassType.CHARGING_STATION)

    tasks = [{'id': 1, 'type': 'fragile', 'shift': 'day'}]
    robots = [Robot(grid, 'R1', 'fragile', 'day', battery_level=3, current_position=(1, 1))]

    task_locations = {
        1: {'pickup': (2, 2), 'dropoff': (3, 3)}
    }
    
    scheduler = Scheduler(grid, tasks, robots, task_locations)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_path_blocked():
    grid = Grid(5, 5)
    for i in range(5):
        grid.set_cell(2, i, ClassType.OBSTACLE)  # vertical wall
    grid.set_cell(2, 2, ClassType.EMPTY)

    tasks = [{'id': 1, 'type': 'standard', 'shift': 'day'}]
    robots = [Robot(grid, 'R1', 'standard', 'day', current_position=(0, 0))]

    task_locations = {
        1: {'pickup': (4, 4), 'dropoff': (0, 4)}
    }

    scheduler = Scheduler(grid, tasks, robots, task_locations)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_robot_competition():
    grid = Grid(7, 7)
    tasks = [{'id': 1, 'type': 'standard', 'shift': 'day'}]

    robots = [
        Robot(grid, 'R1', 'standard', 'day', battery_level=100, current_position=(6, 6)),
        Robot(grid, 'R2', 'standard', 'day', battery_level=100, current_position=(0, 0)),
    ]

    task_locations = {
        1: {'pickup': (3, 3), 'dropoff': (6, 6)}
    }

    scheduler = Scheduler(grid, tasks, robots, task_locations)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_task_overload():
    grid = Grid(6, 6)

    tasks = [
        {'id': 1, 'type': 'fragile', 'shift': 'day'},
        {'id': 2, 'type': 'fragile', 'shift': 'day'},
        {'id': 3, 'type': 'fragile', 'shift': 'day'}
    ]

    robots = [
        Robot(grid, 'R1', 'fragile', 'day', current_position=(0, 0)),
        Robot(grid, 'R2', 'fragile', 'day', current_position=(5, 5))
    ]

    task_locations = {
        1: {'pickup': (1, 1), 'dropoff': (2, 2)},
        2: {'pickup': (3, 3), 'dropoff': (4, 4)},
        3: {'pickup': (0, 5), 'dropoff': (5, 0)}
    }

    scheduler = Scheduler(grid, tasks, robots, task_locations)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

def simulate_type_or_shift_mismatch():
    grid = Grid(5, 5)

    tasks = [{'id': 1, 'type': 'heavy', 'shift': 'night'}]
    robots = [Robot(grid, 'R1', 'standard', 'day', current_position=(0, 0))]

    task_locations = {
        1: {'pickup': (1, 1), 'dropoff': (2, 2)}
    }

    scheduler = Scheduler(grid, tasks, robots, task_locations)
    assignments = scheduler.compute_global_optimal_schedule()
    scheduler.print_schedule(assignments)

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

if __name__ == "__main__":
    run_all_tests()
