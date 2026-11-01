"""
Q8: Filter dictionary entries whose values satisfy a condition without dict comprehension.
"""

def filter_by_value_threshold(d, threshold):
    filtered = {}
    for k in d:
        if d[k] >= threshold:
            filtered[k] = d[k]
    return filtered

if __name__ == "__main__":
    grades = {"Math": 85, "Science": 92, "History": 65, "Art": 78}
    print("Scores >= 80:", filter_by_value_threshold(grades, 80))
