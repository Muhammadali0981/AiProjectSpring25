from typing import Union
from fastapi import FastAPI
from warehouse_system.grid import Grid

app = FastAPI()

@app.get("/api/init")
def init_grid(width: int = 5, height: int = 5):
  grid = Grid(width, height)
  return {"grid": grid.serialize()}

# add robot method
# take robot params from body, make new class and return in "robot" alongside "grid"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}
