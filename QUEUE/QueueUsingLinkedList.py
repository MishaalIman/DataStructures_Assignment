class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self):
        self.front = self.rear = None

    # Enqueue operation
    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # Dequeue operation
    def dequeue(self):
        if not self.front:
            print("Queue is empty.")
            return None
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Peek front element
    def peek(self):
        return self.front.data if self.front else None


# Example usage:
queue = QueueUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Dequeued:", queue.dequeue())  # 10
print("Front:", queue.peek())  # 20
