"""
Q8: Print all prime numbers in a given range [start, end] using nested loops.
"""

def primes_in_range(start, end):
    primes = []
    num = start
    while num <= end:
        if num > 1:
            is_p = True
            d = 2
            while d * d <= num:
                if num % d == 0:
                    is_p = False
                    break
                d += 1
            if is_p:
                primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    print("Primes between 10 and 50:", primes_in_range(10, 50))
