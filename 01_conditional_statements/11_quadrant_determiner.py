"""
Q11: Determine which Cartesian quadrant a point (x, y) lies in or if it lies on an axis / origin.
"""

def find_quadrant(x, y):
    if x == 0 and y == 0:
        return "Origin (0, 0)"
    elif x == 0:
        return "Y-axis"
    elif y == 0:
        return "X-axis"
    elif x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    else:
        return "Quadrant IV"

if __name__ == "__main__":
    print("(3, 4):", find_quadrant(3, 4))
    print("(-2, 5):", find_quadrant(-2, 5))
    print("(-3, -7):", find_quadrant(-3, -7))
    print("(5, -1):", find_quadrant(5, -1))
    print("(0, 5):", find_quadrant(0, 5))
