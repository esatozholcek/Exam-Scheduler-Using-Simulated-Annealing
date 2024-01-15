class Schedule:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.weeks = ["Week1"]
        self.time_slots = [
            "8:00 AM - 10:00 AM",
            "10:30 AM - 12:30 PM",
            "1:00 PM - 2:00 PM",
            "2:30 PM - 4:30 PM",
            "5:00 PM - 6:00 PM",
            "6:30 PM - 8:30 PM",
        ]
        self.schedule = {week: {day: {slot: None for slot in self.time_slots} for day in self.days} for week in self.weeks}
        

    def assign_exam_time(self, course, day, time_slot, room,week):
        self.schedule[week][day][time_slot] = f"{time_slot}: {course.course_id} - Room {room.room_id}"

    def block_hours(self, day, start_time, end_time, reason,week):
        self.schedule[week][day][f"{start_time} - {end_time}"] = f"Blocked: {reason}"