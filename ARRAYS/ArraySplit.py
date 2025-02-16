def split_array(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

# Example Usage:
arr = [1, 2, 3, 4, 5, 6]
print(split_array(arr))  # Output: ([1, 2, 3], [4, 5, 6])
