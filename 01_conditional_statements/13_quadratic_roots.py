"""
Q13: Determine nature and values of quadratic equation roots (ax^2 + bx + c = 0)
without built-in math module.
"""

def square_root_approx(val):
    if val < 0:
        return None
    if val == 0:
        return 0.0
    guess = val / 2.0
    for _ in range(20):
        guess = (guess + val / guess) / 2.0
    return guess

def quadratic_roots(a, b, c):
    if a == 0:
        if b == 0:
            return "Not an equation"
        return f"Linear equation root: {-c / b}"
    
    discriminant = (b * b) - (4 * a * c)
    
    if discriminant > 0:
        sqrt_d = square_root_approx(discriminant)
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
        return f"Two real distinct roots: {r1} and {r2}"
    elif discriminant == 0:
        r = -b / (2 * a)
        return f"Two real equal roots: {r}"
    else:
        return "Complex / Imaginary roots"

if __name__ == "__main__":
    print(quadratic_roots(1, -5, 6))
    print(quadratic_roots(1, -2, 1))
    print(quadratic_roots(1, 1, 1))
