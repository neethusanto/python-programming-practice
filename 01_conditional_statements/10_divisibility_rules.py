"""
Q10: Check if a number is divisible by both 5 and 11, or only one, or neither.
"""

def check_divisibility_5_11(n):
    div5 = (n % 5 == 0)
    div11 = (n % 11 == 0)
    
    if div5 and div11:
        return "Divisible by both 5 and 11"
    elif div5:
        return "Divisible by 5 only"
    elif div11:
        return "Divisible by 11 only"
    else:
        return "Not divisible by 5 or 11"

if __name__ == "__main__":
    for val in [55, 25, 22, 14]:
        print(f"{val}: {check_divisibility_5_11(val)}")
