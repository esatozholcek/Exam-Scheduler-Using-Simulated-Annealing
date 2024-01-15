from src.csv_reader import read_class_list, read_classrooms, get_course_statistics
from src.scheduler import Scheduler
from src.SimulatedAnnealing import SimulatedAnnealing

def day_to_numeric(day):
    # Map days to numeric values for sorting
    days_mapping = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    return days_mapping[day]

def validate_time_input(time_str):
    time_slots = [
        "08:00 AM - 10:00 AM",
        "10:30 AM - 12:30 PM",
        "01:00 PM - 02:00 PM",
        "02:30 PM - 04:30 PM",
        "05:00 PM - 06:00 PM",
        "06:30 PM - 08:30 PM",
    ]

    return time_str in time_slots

def validate_day(day):
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day.capitalize() in valid_days

def main():
    class_list = read_class_list('data/class_list.csv')
    classroom_capacities = read_classrooms('data/classroom.csv')
    course_statics = get_course_statistics(class_list)
    # blocked_hours = [
    #      ("Wednesday", "02:30 PM", "04:30 PM", "Common Course (TİT102)"),
        
    # ]
    
    num_blocked_hours = int(input("Enter the number of blocked hours: "))
    blocked_hours = []
    
    for _ in range(num_blocked_hours):
        day = input("Enter the day: ")
        
        while not validate_day(day):
            print("Invalid day. Please enter a valid day (e.g., Monday, Tuesday)")
            day = input("Enter the day: ")
            
        start_time = input("Enter the start time (e.g., 02:30 PM): ")
        end_time = input("Enter the end time (e.g., 04:30 PM): ")
        
        time_slot = f"{start_time} - {end_time}"

        while not validate_time_input(time_slot):
            print("Invalid time. Please enter a valid time slot.")
            start_time = input("Enter the start time (e.g., 02:30 PM): ")
            end_time = input("Enter the end time (e.g., 04:30 PM): ")
            time_slot = f"{start_time} - {end_time}"
            
        course_name = input("Enter the course name: ")
        blocked_hours.append((day.capitalize(), start_time, end_time, course_name))

    
    
    scheduler = Scheduler(course_statics, classroom_capacities, blocked_hours)
    simulated_annealing_result = SimulatedAnnealing.run(scheduler, initial_temperature=100, cooling_rate=0.95, iterations=1000)

    # Sorting the result based on the day (Monday to Sunday)
    sorted_result = sorted(simulated_annealing_result.items(), key=lambda x: day_to_numeric(x[1]['day']))

    print()
    for index, course_info in sorted_result:
        day = course_info['day'][0:10]
        time_slot = course_info['time_slot']
        lesson = course_info['course'] 
        week = course_info['week']

        print(f"Day: {day:<12} Time: {time_slot:<22} Lesson: {lesson:<12} Week: {week:<8} Rooms: {course_info['rooms']}")
    print("Blocked hour is ", blocked_hours)
if __name__ == '__main__':
    main()