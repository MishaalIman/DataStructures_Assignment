class StackArray:
    def __init__(self, capacity=10):
        self.stack = []
        self.capacity = capacity

    def push(self, data):
        if len(self.stack) >= self.capacity:
            return "Stack Overflow"
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack (top to bottom):", self.stack[::-1])

# Example Usage:
stack = StackArray(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: Stack (top to bottom): [30, 20, 10]
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
