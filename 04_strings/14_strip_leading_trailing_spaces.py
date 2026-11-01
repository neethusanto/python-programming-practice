"""
Q14: Strip leading and trailing whitespace characters without using str.strip().
"""

def custom_strip(s):
    n = 0
    for _ in s:
        n += 1
        
    start = 0
    while start < n and (s[start] == ' ' or s[start] == '\t' or s[start] == '\n'):
        start += 1
        
    end = n - 1
    while end >= start and (s[end] == ' ' or s[end] == '\t' or s[end] == '\n'):
        end -= 1
        
    result = ""
    idx = start
    while idx <= end:
        result += s[idx]
        idx += 1
    return result

if __name__ == "__main__":
    s = "   Hello World!   "
    print(f"Stripped: '{custom_strip(s)}'")
