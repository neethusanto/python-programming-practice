"""
Q12: Filter prime numbers up to N using list comprehension with a prime-check helper.
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

def primes_up_to_n(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

if __name__ == "__main__":
    print("Primes up to 50:", primes_up_to_n(50))
