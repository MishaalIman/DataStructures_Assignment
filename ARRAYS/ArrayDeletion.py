def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of range"
    return arr[:index] + arr[index+1:]

# Example Usage:
arr = [1, 2, 3, 4, 5]
print(delete_element(arr, 2))  # Output: [1, 2, 4, 5]
