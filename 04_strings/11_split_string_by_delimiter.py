"""
Q11: Split a string by a delimiter without using str.split().
"""

def custom_split(s, delimiter=' '):
    parts = []
    current_token = ""
    for ch in s:
        if ch == delimiter:
            parts.append(current_token)
            current_token = ""
        else:
            current_token += ch
    parts.append(current_token)
    return parts

if __name__ == "__main__":
    text = "apple,banana,cherry,dates"
    print("Custom split:", custom_split(text, ','))
