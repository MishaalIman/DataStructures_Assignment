class QueueUsingArray:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    # Enqueue operation
    def enqueue(self, item):
        if len(self.queue) >= self.capacity:
            print("Queue is full.")
            return
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation
    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue.pop(0)

    # Peek front element
    def front(self):
        return self.queue[0] if self.queue else None

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
queue = QueueUsingArray(5)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print("Dequeued:", queue.dequeue())  # 5
print("Front:", queue.front())  # 10
