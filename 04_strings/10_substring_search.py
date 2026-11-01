"""
Q10: Search for a substring within a main string without using 'in', find(), or index().
Returns starting index if found, else -1.
"""

def substring_search(main_str, sub_str):
    m_len = 0
    for _ in main_str:
        m_len += 1
        
    s_len = 0
    for _ in sub_str:
        s_len += 1
        
    if s_len == 0:
        return 0
    if s_len > m_len:
        return -1
        
    i = 0
    while i <= m_len - s_len:
        match = True
        j = 0
        while j < s_len:
            if main_str[i + j] != sub_str[j]:
                match = False
                break
            j += 1
        if match:
            return i
        i += 1
        
    return -1

if __name__ == "__main__":
    text = "Welcome to python basics"
    print("Find 'python':", substring_search(text, "python"))
    print("Find 'java':", substring_search(text, "java"))
