from src.csv_reader import read_class_list, read_classrooms, get_course_statistics
from src.scheduler import Scheduler
from src.SimulatedAnnealing import SimulatedAnnealing

def day_to_numeric(day):
    # Map days to numeric values for sorting
    days_mapping = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    return days_mapping[day]

def main():
    class_list = read_class_list('data/class_list.csv')
    classroom_capacities = read_classrooms('data/classroom.csv')
    course_statics = get_course_statistics(class_list)
    blocked_hours = [
         ("Wednesday", "2:30 PM", "4:30 PM", "Common Course (TİT102)"),
        
    ]
    
    
    scheduler = Scheduler(course_statics, classroom_capacities, blocked_hours)
    simulated_annealing_result = SimulatedAnnealing.run(scheduler, initial_temperature=100, cooling_rate=0.95, iterations=1000)

    # Sorting the result based on the day (Monday to Sunday)
    sorted_result = sorted(simulated_annealing_result.items(), key=lambda x: day_to_numeric(x[1]['day']))

    for index, course_info in sorted_result:
        day = course_info['day'][0:10]
        time_slot = course_info['time_slot']
        lesson = course_info['course'] 
        week = course_info['week']

        print(f"Day: {day}, Time: {time_slot}, Lesson: {lesson}, Week: {week}, Rooms: {course_info['rooms']}")
    print("Blocked hour is ", blocked_hours)
if __name__ == '__main__':
    main()