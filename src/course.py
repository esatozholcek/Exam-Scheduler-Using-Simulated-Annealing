

class Course:
    def __init__(self, student_id, professor_name, course_id, duration):
        self.student_id = student_id
        self.professor_name = professor_name
        self.course_id = course_id
        self.duration = duration
        

    def __str__(self):
        return f"{self.course_id} - {self.professor_name}"