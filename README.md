# Warehouse Robot Scheduling and Visualization System
## Demo Video
[![image](https://github.com/user-attachments/assets/bacbb3a7-6046-41c3-8a17-475e62ec41b3)](https://drive.google.com/file/d/1qPds7T_PVsJfW0BGZGB1oQ05j5uFf7ec/view?usp=sharing)
## Project Description

This project is a comprehensive warehouse robot scheduling and visualization system. It consists of a Python-based backend (FastAPI) that models a warehouse environment, robots, and tasks, and a modern React + TypeScript frontend for interactive visualization and management. The system allows users to:
- Design and configure a warehouse grid with obstacles, ramps, slopes, charging stations, and boxes.
- Add and configure robots with different types and shifts.
- Create and assign tasks with pickup and dropoff locations.
- Run an optimal scheduling algorithm (using Google OR-Tools) to assign robots to tasks, considering battery, compatibility, and pathfinding constraints.
- Visualize the warehouse state and scheduling results interactively.

---

## Features

### Backend (Python, FastAPI)
- **Warehouse Modeling:** Flexible grid with cell types (empty, obstacle, ramp, slope, charging station, box, robot).
- **Robot & Task Management:** Multiple robot types (general, standard, fragile), shifts (day, night, 24/7), and task types (standard, heavy, fragile).
- **Optimal Scheduling:** Uses Google OR-Tools CP-SAT solver to assign robots to tasks, minimizing battery usage and maximizing assignments.
- **Pathfinding:** A* search for robot movement, considering obstacles and cell types.
- **Battery & Charging Logic:** Robots may need to visit charging stations if battery is insufficient for a task.
- **REST API:** Endpoints for initializing the warehouse, adding robots/cells/tasks, and running the scheduler.

### Frontend (React, TypeScript, Vite)
- **Interactive Grid Visualization:** Drag-and-drop interface to edit the warehouse grid, place robots, and assign tasks.
- **Robot & Task Editors:** UI for configuring robot types, shifts, and task parameters.
- **Scheduling Visualization:** Run the scheduler and see assignments and robot paths.
- **Modern UI:** Built with Radix UI, Tailwind CSS, and Framer Motion for smooth, accessible interactions.

---

## Setup Instructions

### Backend
1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

---

## Libraries Used

### Backend (Python)
- fastapi
- uvicorn
- starlette
- pydantic
- ortools
- numpy
- pandas
- python-dotenv
- requests
- rich
- email_validator
- python-multipart
- Jinja2
- and others (see `backend/requirements.txt` for full list)

### Frontend (JavaScript/TypeScript)
- react
- react-dom
- vite
- @radix-ui/react-* (context-menu, dialog, dropdown-menu, label, select, slot)
- @react-three/fiber, @react-three/drei, three (for 3D visualization)
- tailwindcss, @tailwindcss/vite, tailwind-merge, tw-animate-css
- axios
- framer-motion
- lucide-react
- next-themes
- sonner
- class-variance-authority, clsx
- and others (see `frontend/package.json` for full list)

---

## Main Modules Overview

### Backend
- `main.py`: FastAPI entry point, defines API endpoints.
- `warehouse_system/`: Core logic for grid, robots, tasks, scheduling, pathfinding, and enums.
- `simulate.py`: Test and simulation scripts for various warehouse scenarios.

### Frontend
- `src/App.tsx`: Main React app entry.
- `src/pages/warehouse.tsx`: Main warehouse visualization and interaction logic.
- `src/components/`: UI components for grid, menus, and controls.

---

## License
This project is for educational and research purposes.
