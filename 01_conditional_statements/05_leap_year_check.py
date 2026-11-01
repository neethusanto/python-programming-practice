"""
Q5: Determine if a year is a leap year.
Rule: Divisible by 4 and not by 100, OR divisible by 400.
"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    for y in [2000, 1900, 2024, 2023]:
        print(f"{y} is leap year: {is_leap_year(y)}")
