"""
Q5: Count the number of digits in an integer without len() or str().
"""

def count_digits(n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

if __name__ == "__main__":
    for num in [0, 7, 245, 100000, -9876]:
        print(f"Digits in {num}: {count_digits(num)}")
