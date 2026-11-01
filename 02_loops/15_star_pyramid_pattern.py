"""
Q15: Print pyramid star pattern using nested loops.
    *
   ***
  *****
 *******
*********
"""

def print_star_pyramid(rows):
    i = 1
    while i <= rows:
        spaces = ""
        s = 1
        while s <= (rows - i):
            spaces = spaces + " "
            s += 1
            
        stars = ""
        st = 1
        while st <= (2 * i - 1):
            stars = stars + "*"
            st += 1
            
        print(spaces + stars)
        i += 1

if __name__ == "__main__":
    print_star_pyramid(5)
