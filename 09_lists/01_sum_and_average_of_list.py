"""
Q1: Calculate sum and average of elements in a list without using sum() or len().
"""

def list_sum_and_avg(items):
    total = 0
    count = 0
    for x in items:
        total += x
        count += 1
    avg = total / count if count > 0 else 0.0
    return total, avg

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    total, avg = list_sum_and_avg(nums)
    print(f"List: {nums} -> Sum: {total}, Average: {avg}")
