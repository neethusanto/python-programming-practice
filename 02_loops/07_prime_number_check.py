"""
Q7: Check whether a given integer is a prime number using a loop.
Constraint: No external libraries.
"""

def is_prime(n):
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

if __name__ == "__main__":
    for val in [1, 2, 3, 4, 17, 25, 29, 97, 100]:
        print(f"{val} is prime: {is_prime(val)}")
