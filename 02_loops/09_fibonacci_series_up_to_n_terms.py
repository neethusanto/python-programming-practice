"""
Q9: Print first N terms of Fibonacci series using a loop.
Constraint: Iterative approach without recursion or built-ins.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    i = 2
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib

if __name__ == "__main__":
    print("First 10 Fibonacci numbers:", generate_fibonacci(10))
