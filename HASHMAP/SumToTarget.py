def sum_to_target(arr, target):
    hashmap = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]  # Return indices
        hashmap[num] = i
    return []  # No solution found

# Example Usage:
arr = [2, 7, 11, 15]
target = 9
print("Indices of sum-to-target:", sum_to_target(arr, target))  # Output: [0, 1]
