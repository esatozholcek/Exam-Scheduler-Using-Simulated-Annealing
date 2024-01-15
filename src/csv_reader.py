import csv

def read_class_list(file_path):
    """
    Read class list from a CSV file and return a list of dictionaries.
    
    Args:
    - file_path (str): Path to the CSV file containing the class list.

    Returns:
    - List of dictionaries: Each dictionary represents a row in the CSV file.
    """
    class_list = []

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            
            for row in csv_reader:
                row = row[0].split(";")
                student_id = row[0]
                professor_name = row[1]
                course_id = row[2]
                exam_duration = int(row[3])

                class_list.append({
                    'StudentID': student_id,
                    'Professor Name': professor_name,
                    'CourseID': course_id,
                    'ExamDuration': exam_duration
                })

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return class_list
    
    
    
    

def read_classrooms(file_path):
    """
    Read classroom capacities from a CSV file and return a list of tuples.
    
    Args:
    - file_path (str): Path to the CSV file containing classroom capacities.

    Returns:
    - List of tuples: Each tuple contains (RoomID, Capacity).
    """
    classroom_capacities = []

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                row = row[0].split(";")
                room_id = row[0]
                capacity = row[1]
                classroom_capacities.append((room_id, int(capacity)))

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

    return classroom_capacities

def get_course_statistics(class_list):
    """
    Get course statistics from the class list.

    Args:
    - class_list (list): List of dictionaries representing the class list.

    Returns:
    - Dictionary: Course statistics with course names as keys and the number of students as values.
    """
    course_statistics = {}

    for entry in class_list:
        course_id = entry['CourseID']

        if course_id not in course_statistics:
            course_statistics[course_id] = 1
        else:
            course_statistics[course_id] += 1

    return course_statistics