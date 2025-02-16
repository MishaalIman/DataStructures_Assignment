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

    # Method to check if the list is circular (loop detection)
    def is_circular(self):
        if not self.head:
            return False

        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            # If slow_ptr and fast_ptr meet, there is a loop (circular)
            if slow_ptr == fast_ptr:
                return True

        return False


# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Checking if the list is circular before making it circular
print("Is the list circular?", ll.is_circular())  # Output: False

# Making the list circular manually
ll.head.next.next.next.next = ll.head.next  # Connecting last node to second node

# Checking again if the list is circular
print("Is the list circular?", ll.is_circular())  # Output: True
