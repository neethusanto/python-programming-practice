"""
Q12: Compute cumulative running sum list without itertools.accumulate.
"""

def cumulative_sum(numbers):
    running_total = 0
    result = []
    for x in numbers:
        running_total += x
        result.append(running_total)
    return result

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Cumulative sum:", cumulative_sum(data))
