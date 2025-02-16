def search_element(arr, value):
    for i, val in enumerate(arr):
        if val == value:
            return i
    return -1  # Not found

# Example Usage:
arr = [10, 20, 30, 40]
print(search_element(arr, 30))  # Output: 2
