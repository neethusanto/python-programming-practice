"""
Q12: Join a list of strings with a separator without using str.join().
"""

def custom_join(strings, separator):
    result = ""
    is_first = True
    for item in strings:
        if is_first:
            result += item
            is_first = False
        else:
            result = result + separator + item
    return result

if __name__ == "__main__":
    words = ["Python", "is", "awesome"]
    print(custom_join(words, " "))
    print(custom_join(words, "---"))
