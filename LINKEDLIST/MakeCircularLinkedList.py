class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to make the list circular by linking last node to a node at the given position
    def make_circular(self, position):
        if position <= 0:
            print("Position should be greater than 0.")
            return

        current = self.head
        count = 1
        while current and count < position:
            current = current.next
            count += 1

        if not current:
            print("Position exceeds the number of nodes.")
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = current  # Making the list circular by linking last node to the node at 'position'
        print(f"Linked list made circular by connecting last node to node at position {position}")


# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Making the list circular at position 2...")
ll.make_circular(2)
