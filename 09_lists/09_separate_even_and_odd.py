"""
Q9: Separate even and odd numbers of a list into two distinct lists.
"""

def separate_even_odd(numbers):
    evens = []
    odds = []
    for x in numbers:
        if x % 2 == 0:
            evens.append(x)
        else:
            odds.append(x)
    return evens, odds

if __name__ == "__main__":
    nums = [12, 17, 24, 35, 42, 51, 60]
    evens, odds = separate_even_odd(nums)
    print("Evens:", evens)
    print("Odds:", odds)
