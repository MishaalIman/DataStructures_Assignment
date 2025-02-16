import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Insert an element with priority
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
        print(f"Enqueued: {item} with priority {priority}")

    # Remove and return the highest priority element (smallest value)
    def dequeue(self):
        if not self.queue:
            print("Priority Queue is empty.")
            return None
        return heapq.heappop(self.queue)[1]

    # Peek at the highest priority element
    def peek(self):
        return self.queue[0][1] if self.queue else None

    # Check if priority queue is empty
    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
pq = PriorityQueue()
pq.enqueue("Task1", 3)
pq.enqueue("Task2", 1)  # Higher priority (smaller number)
pq.enqueue("Task3", 2)

print("Dequeued:", pq.dequeue())  # Task2 (highest priority)
print("Front:", pq.peek())  # Task3
