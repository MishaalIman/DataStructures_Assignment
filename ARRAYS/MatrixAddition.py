def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example Usage:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(add_matrices(A, B))  # Output: [[6, 8], [10, 12]]
