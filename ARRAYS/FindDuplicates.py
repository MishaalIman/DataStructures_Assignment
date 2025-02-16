def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

# Example Usage:
arr = [1, 2, 3, 4, 2, 3, 5]
print(find_duplicates(arr))  # Output: [2, 3]
