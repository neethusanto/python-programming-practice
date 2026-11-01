"""
Q8: Calculate letter grade based on marks (0 to 100).
"""

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail (F)"

if __name__ == "__main__":
    for score in [95, 82, 74, 63, 51, 42, 105]:
        print(f"Score {score}: {calculate_grade(score)}")
