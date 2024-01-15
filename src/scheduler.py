import random
import math

from src.schedule import Schedule

#This class about methods which are used in simulated anneling algorithm occurs from generate_initial_solution , calculate_energy, generate_neighbor_solution and update_solution
class Scheduler:
    #this is the base constructor
    def __init__(self, courses, classrooms, blocked_hours):
        self.courses = courses
        self.classrooms = classrooms
        self.blocked_hours = blocked_hours
        self.schedule = Schedule()
    
    #this methods make inital solution for simulated anneling.
    def generate_initial_solution(self):
        initial_solution = {}
        #take random of each element which is taken from list
        for index, course in enumerate(self.courses):
            day = random.choice(self.schedule.days)
            time_slot = random.choice(self.schedule.time_slots)
            room = random.choice(self.classrooms)
            week = random.choice(self.schedule.weeks)
            
            #capacity of the course. Number of students which takes the course
            course_capacity = self.courses[course] 
            
            # If room capacity is less than twice the course capacity, keep trying until a suitable room is found
            while (room[1] / 2) < course_capacity:
                additional_room = random.choice(self.classrooms)
                
                
                total_capacity = (room[1] + additional_room[1]) / 2
                if total_capacity >= course_capacity and additional_room[1] is not room[1]:
        
                    initial_solution[index] = {'day': day, 'time_slot': time_slot, 'rooms': [room, additional_room], 'course': course, 'week': week}
                    break
                else:
                    
                    
                    room = random.choice(self.classrooms)
                    continue
            # print the solution if it is not found in while    
            else:
                initial_solution[index] = {'day': day, 'time_slot': time_slot, 'rooms': [room], 'course': course, 'week': week}
                
        return initial_solution

    #this methods calculates energy so it calculates the mistakes in the schedule and we have to minimize the energy 
    def calculate_energy(self, solution):
        conflicts = 0
        course_values = list(solution.values())

        for i in range(len(course_values)):
            for j in range(i + 1, len(course_values)):
                course1 = course_values[i]
                course2 = course_values[j]

                if (
                    course1['week'] == course2['week'] and
                    course1['day'] == course2['day'] and
                    course1['time_slot'] == course2['time_slot'] and
                    any(room in course2['rooms'] for room in course1['rooms'])
                    
                ):
                    conflicts += 1

        return conflicts
    
    #if there is energy so it is different than 0 find the other solutions for minimizing energy 
    def generate_neighbor_solution(self, current_solution):
        neighbor_solution = current_solution.copy()
        random_course_index = random.choice(list(neighbor_solution.keys()))
        random_course = neighbor_solution[random_course_index]['course']

       
        existing_course_details = neighbor_solution[random_course_index]

        #take random elements from our lists
        day, time_slot, room, week = (
            random.choice(self.schedule.days),
            random.choice(self.schedule.time_slots),
            random.choice(self.classrooms),
            random.choice(self.schedule.weeks)
        )

        course_capacity = self.courses[random_course]

       # If room capacity is less than twice the course capacity, keep trying until a suitable room is found
        while (room[1] / 2) < course_capacity:
            additional_room = random.choice(self.classrooms)
        
            
            total_capacity = (room[1] + additional_room[1]) / 2
            if total_capacity >= course_capacity and additional_room[1] is not room[1]:
               
                neighbor_solution[random_course_index] = {'course': random_course, 'day': day, 'time_slot': time_slot, 'rooms': [room, additional_room], 'week': week}
                break
            else:
                
                room = random.choice(self.classrooms)
                continue
    
        else:
            neighbor_solution[random_course_index] = {'course': random_course, 'day': day, 'time_slot': time_slot, 'rooms': [room], 'week': week}

        return neighbor_solution
    
    #update the last solution
    def update_solution(self, new_solution):
        self.schedule = Schedule()
        for course, (day, time_slot, room) in new_solution.items():
            self.schedule.assign_exam_time(course, day, time_slot, room)
        for day, start_time, end_time, reason in self.blocked_hours:
            self.schedule.block_hours(day, start_time, end_time, reason)
