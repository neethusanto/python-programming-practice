"""
Q5: Extract dates matching DD/MM/YYYY or DD-MM-YYYY formats.
"""
import re

def extract_dates(text):
    pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = "Events are scheduled on 15/08/2026, 01-01-2027 and 31/12/2025."
    print("Dates found:", extract_dates(sample))
