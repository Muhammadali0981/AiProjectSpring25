class Robot:
    def __init__(self, robot_id: str, robot_type: str, shift: str, battery_level: int = 100, current_position: tuple = (0, 0)):
        self.robot_id = robot_id
        self.robot_type = robot_type
        self.shift = shift
        self.battery_level = battery_level
        self.is_carrying_box = False
        self.current_position = current_position

    def charge(self):
        self.battery_level = 100
        
    def serialize(self):
        return {
            "robot_id": self.robot_id,
            "robot_type": self.robot_type,
            "shift": self.shift,
            "battery_level": self.battery_level,
            "is_carrying_box": self.is_carrying_box,
            "current_position": list(self.current_position)
        }
    
    @classmethod
    def deserialize(cls, data: dict):
        return cls(
            data["robot_id"],
            data["robot_type"],
            data["shift"],
            data["battery_level"],
            tuple(data["current_position"])
        )
