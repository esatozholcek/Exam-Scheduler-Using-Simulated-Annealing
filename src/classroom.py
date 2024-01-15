# This class for representing a classroom with a room ID and capacity
class Classroom:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity

    def __str__(self):
        return f"{self.room_id} - Capacity: {self.capacity}"
