"""
Q15: Calculate income tax based on income slabs without built-ins.
Slabs:
- Up to 250000: 0%
- 250001 to 500000: 5%
- 500001 to 1000000: 20%
- Above 1000000: 30%
"""

def calculate_income_tax(income):
    if income <= 250000:
        tax = 0.0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
    return tax

if __name__ == "__main__":
    for inc in [200000, 400000, 750000, 1500000]:
        print(f"Income: {inc} => Tax: {calculate_income_tax(inc)}")
