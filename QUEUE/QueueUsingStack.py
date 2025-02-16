class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Enqueue operation (efficient)
    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation (costly)
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty.")
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Check if queue is empty
    def is_empty(self):
        return not self.stack1 and not self.stack2

    # Peek front element
    def front(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty.")
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]


# Example usage:
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())  # 1
print("Front:", queue.front())  # 2
