def insert_element(arr, index, value):
    if index < 0 or index > len(arr):
        return "Index out of range"
    return arr[:index] + [value] + arr[index:]

# Example Usage:
arr = [1, 2, 4, 5]
print(insert_element(arr, 2, 3))  # Output: [1, 2, 3, 4, 5]
