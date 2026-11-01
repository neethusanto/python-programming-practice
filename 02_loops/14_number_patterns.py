"""
Q14: Print number patterns using nested loops.
Pattern 1: Right triangle of numbers
1
1 2
1 2 3
1 2 3 4
"""

def print_number_triangle(rows):
    i = 1
    while i <= rows:
        j = 1
        line = ""
        while j <= i:
            line = line + str(j) + " "
            j += 1
        print(line)
        i += 1

if __name__ == "__main__":
    print_number_triangle(5)
