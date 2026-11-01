"""
Q12: Simple calculator using if-elif-else without eval().
Supports operators: '+', '-', '*', '/', '%'
"""

def calculate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif op == '%':
        if num2 == 0:
            return "Error: Modulo by zero"
        return num1 % num2
    else:
        return "Invalid Operator"

if __name__ == "__main__":
    print("10 + 5 =", calculate(10, '+', 5))
    print("10 - 3 =", calculate(10, '-', 3))
    print("10 * 4 =", calculate(10, '*', 4))
    print("10 / 2 =", calculate(10, '/', 2))
    print("10 / 0 =", calculate(10, '/', 0))
