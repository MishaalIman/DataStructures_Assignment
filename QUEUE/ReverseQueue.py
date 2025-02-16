from collections import deque

def reverse_queue(queue):
    stack = []
    while queue:
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

# Example usage:
queue = deque([1, 2, 3, 4, 5])
reverse_queue(queue)
print("Reversed Queue:", list(queue))  # Output: [5, 4, 3, 2, 1]
