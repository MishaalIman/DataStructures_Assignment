from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q1.put(x)

    def pop(self):
        if self.q1.empty():
            return None
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        popped_element = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return popped_element

    def top(self):
        if self.q1.empty():
            return None
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        top_element = self.q1.get()
        self.q2.put(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self):
        return self.q1.empty()

# Example usage:
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
print(stack.pop())  # Output: 1
print(stack.empty())  # Output: True