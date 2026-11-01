"""
Q7: Flatten a 2D matrix (list of lists) into a 1D list using nested list comprehension.
"""

def flatten_matrix(matrix):
    return [val for row in matrix for val in row]

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Flattened matrix:", flatten_matrix(mat))
