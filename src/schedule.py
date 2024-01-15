class Schedule:
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]   #Initialization part for class
        self.weeks = ["Week1"]
        self.time_slots = [
            "8:00 AM - 10:00 AM",
            "10:30 AM - 12:30 PM",
            "1:00 PM - 2:00 PM",
            "2:30 PM - 4:30 PM",
            "5:00 PM - 6:00 PM",
            "6:30 PM - 8:30 PM",
        ] #We defined the possible time slots for the exams
        self.schedule = {week: {day: {slot: None for slot in self.time_slots} for day in self.days} for week in self.weeks}


   