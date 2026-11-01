"""
Q12: Calculate total sum of all numeric values in a dictionary without sum() or values().
"""

def sum_dict_values(d):
    total = 0
    for k in d:
        total += d[k]
    return total

if __name__ == "__main__":
    expenses = {"rent": 1200, "groceries": 450, "utilities": 180, "internet": 60}
    print("Total expenses:", sum_dict_values(expenses))
