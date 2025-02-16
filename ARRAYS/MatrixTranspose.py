def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Example Usage:
A = [[1, 2], [3, 4]]
print(transpose_matrix(A))  # Output: [[1, 3], [2, 4]]
