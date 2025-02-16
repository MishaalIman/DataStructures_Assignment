class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.capacity = capacity

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def front_element(self):
        return self.queue[self.front] if self.front != -1 else None


# Example usage:
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

print("Dequeued:", cq.dequeue())  # 10
print("Front:", cq.front_element())  # 20
