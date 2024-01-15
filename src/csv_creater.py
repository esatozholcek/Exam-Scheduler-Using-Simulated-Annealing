import pandas as pd
import csv
from src.course import Course
import random
import numpy as np
import matplotlib.pyplot as plt


class CsvCreator:
    def __init__(self):
        self.students = []
        self.courses = []
        self.__read_file()
    
    def __read_file(self):
        with open("data\courses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                row = row[0].split(";")
                self.courses.append(Course(row[0], int(row[1]), int(row[2]), int(row[3]), row[4]))
        
        
        courses_copy = self.courses.copy()
        for i in range(4):
            for j in range(100):
                self.students.append(Student(1001 + (i * 100) + j, i+1))
                
        normal_distribution = np.random.normal(0, 1, 1000)
        normal_distribution = normal_distribution / 3.0
        
        
        for i in range(400):
            available_year_courses = ["ceng"]
            while (len(self.students[i].take_courses) < 5 and (len(available_year_courses) > 0)):
                rand = normal_distribution[random.randint(0, 999)]    
                year = max(round(self.students[i].grade + rand), 1)
                print(f"year: {year} rand: {rand} id: {i}")
                
                available_year_courses = [course for course in courses_copy if course.year == self.students[i].grade and course not in self.students[i].take_courses]
                available_courses = [course for course in courses_copy if course.year == year and course not in self.students[i].take_courses]
                print(f"len take courses: {len(self.students[i].take_courses)} available course: {len(available_courses)} id: {i}")
                if len(available_courses) == 0:
                    continue
                
                index = random.randint(0, len(available_courses) - 1)
                self.students[i].take_courses.append(available_courses[index])
                courses_copy[courses_copy.index(available_courses[index])].num_of_students -= 1
                
                if courses_copy[courses_copy.index(available_courses[index])].num_of_students == 0:
                    courses_copy.remove(available_courses[index])
                
        print()
        for course in courses_copy:
            print(course)
            
        for i in range(400):
            print(f"id: {1001+i} num of take courses: {len(self.students[i].take_courses)}")

        print("deneme")
        
        for i in range(399, 299, -1):
            print(i)
            available_courses = [course for course in courses_copy if (course.year == 2 or course.year == 3) and course not in self.students[i].take_courses]
            print(len(available_courses))
            print("Available courses: ")
            
            for i in range(len(available_courses)):
                print(available_courses[i])
                
            print(f"Taken courses with length {len(self.students[i].take_courses)} ")
            for i in range(len(self.students[i].take_courses)):
                print(self.students[i].take_courses[i])
                
                
            while (len(self.students[i].take_courses) < 5 and (len(available_courses) > 0)):
                index = random.randint(0, len(available_courses) - 1)
                if available_courses[index] not in self.students[i].take_courses:
                    self.students[i].take_courses.append(available_courses[index])
                    courses_copy[courses_copy.index(available_courses[index])].num_of_students -= 1
                
                if courses_copy[courses_copy.index(available_courses[index])].num_of_students == 0:
                    courses_copy.remove(available_courses[index])
                    available_courses.remove(available_courses[index])
                    
                    
        # writing course_list.csv file
        with open("data\class_list.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            
            for i in range(400):
                for course in self.students[i].take_courses:
                    # Use writerow with a list to ensure proper semicolon separation
                    writer.writerow([self.students[i].ID, course.prof_name, course.course_ID, course.duration_course])
            
        

    



