"""
Q13: Extract all numeric digits from an alphanumeric string as integers using list comprehension.
"""

def extract_digits(text):
    return [int(ch) for ch in text if '0' <= ch <= '9']

if __name__ == "__main__":
    text = "Room 404, Building 12, Floor 3"
    print("Extracted digits:", extract_digits(text))
