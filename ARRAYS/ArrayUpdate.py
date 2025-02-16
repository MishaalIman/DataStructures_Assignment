def update_element(arr, index, value):
    if index < 0 or index >= len(arr):
        return "Index out of range"
    arr[index] = value
    return arr

# Example Usage:
arr = [1, 2, 3, 4, 5]
print(update_element(arr, 2, 9))  # Output: [1, 2, 9, 4, 5]
