"""
Q6: Classify a triangle as Equilateral, Isosceles, Scalene, or Invalid given 3 side lengths.
"""

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid Triangle"
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid Triangle"
    
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

if __name__ == "__main__":
    print("3, 3, 3:", classify_triangle(3, 3, 3))
    print("3, 3, 5:", classify_triangle(3, 3, 5))
    print("3, 4, 5:", classify_triangle(3, 4, 5))
    print("1, 2, 10:", classify_triangle(1, 2, 10))
