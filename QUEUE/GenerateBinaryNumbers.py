from collections import deque

def generate_binary_numbers(n):
    queue = deque()
    queue.append("1")
    result = []

    for _ in range(n):
        front = queue.popleft()
        result.append(front)
        queue.append(front + "0")
        queue.append(front + "1")

    return result

# Example usage:
n = 5
print("Binary Numbers:", generate_binary_numbers(n))  # ['1', '10', '11', '100', '101']
