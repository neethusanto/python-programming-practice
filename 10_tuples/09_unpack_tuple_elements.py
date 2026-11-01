"""
Q9: Unpack a tuple of values into distinct variables and display them.
"""

def unpack_student(student_record):
    name, age, course, marks = student_record
    return {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

if __name__ == "__main__":
    record = ("Alex", 20, "Computer Science", 92.5)
    print("Unpacked student:", unpack_student(record))
