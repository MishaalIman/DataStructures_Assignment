def rotate_array(arr, k):
    k = k % len(arr)  # Handles cases where k > len(arr)
    return arr[k:] + arr[:k]

# Example Usage:
arr = [1, 2, 3, 4, 5]
print(rotate_array(arr, 2))  # Output: [3, 4, 5, 1, 2]
