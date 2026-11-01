"""
Q9: Check if a person is eligible to vote (age >= 18).
"""

def check_voting_eligibility(age):
    if age < 0:
        return "Invalid Age"
    elif age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

if __name__ == "__main__":
    print("Age 21:", check_voting_eligibility(21))
    print("Age 15:", check_voting_eligibility(15))
    print("Age -3:", check_voting_eligibility(-3))
