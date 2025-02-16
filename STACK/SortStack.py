def sorted_insert(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)

# Example Usage:
stack = [34, 3, 31, 98, 92, 23]
sort_stack(stack)
print(stack)  # Output: [3, 23, 31, 34, 92, 98]
