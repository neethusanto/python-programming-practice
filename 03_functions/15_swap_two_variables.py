"""
Q15: Write a function that demonstrates swapping two variables without temporary variable
and without tuple assignment packaging.
"""

def swap_arithmetic(a, b):
    # Using arithmetic additions and subtractions
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap_bitwise_xor(a, b):
    # Using bitwise XOR for integers
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    x, y = 15, 42
    print(f"Original: x={x}, y={y}")
    x, y = swap_arithmetic(x, y)
    print(f"Swapped (Arithmetic): x={x}, y={y}")
    x, y = swap_bitwise_xor(x, y)
    print(f"Swapped back (XOR): x={x}, y={y}")
