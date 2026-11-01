"""
Q8: Transpose a matrix (swap rows and columns) using nested list comprehension.
"""

def transpose_matrix(matrix):
    num_cols = len(matrix[0])
    num_rows = len(matrix)
    return [[matrix[r][c] for r in range(num_rows)] for c in range(num_cols)]

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print("Transposed matrix:", transpose_matrix(mat))
