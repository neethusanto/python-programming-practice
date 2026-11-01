"""
Q11: Check if a number is an Armstrong number (sum of each digit raised to power of num_digits).
Constraint: Compute digit count and power manually using loops.
"""

def power(base, exp):
    res = 1
    i = 0
    while i < exp:
        res *= base
        i += 1
    return res

def is_armstrong(n):
    if n < 0:
        return False
    
    temp = n
    digit_count = 0
    if temp == 0:
        digit_count = 1
    else:
        while temp > 0:
            digit_count += 1
            temp = temp // 10
            
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += power(digit, digit_count)
        temp = temp // 10
        
    return total == n

if __name__ == "__main__":
    for val in [153, 370, 371, 9474, 123]:
        print(f"{val} is Armstrong: {is_armstrong(val)}")
