def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return reversed_s

# Example Usage:
s = "hello"
print(reverse_string(s))  # Output: "olleh"
