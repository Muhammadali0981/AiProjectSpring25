class Task:
  def __init__(self, task_id: int, type: str, shift: str, pickup_location: tuple, dropoff_location: tuple):
    self.task_id = task_id
    self.type = type
    self.shift = shift
    self.pickup_location = pickup_location
    self.dropoff_location = dropoff_location

  def serialize(self):
    return {
      "task_id": self.task_id,
      "type": self.type,
      "shift": self.shift,
      "pickup_location": list(self.pickup_location),
      "dropoff_location": list(self.dropoff_location)
    }

  @classmethod
  def deserialize(cls, data: dict):
    return cls(data["task_id"], data["type"], data["shift"], data["pickup_location"], data["dropoff_location"])
  