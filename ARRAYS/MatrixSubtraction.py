def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Example Usage:
A = [[5, 6], [7, 8]]
B = [[1, 2], [3, 4]]
print(subtract_matrices(A, B))  # Output: [[4, 4], [4, 4]]
