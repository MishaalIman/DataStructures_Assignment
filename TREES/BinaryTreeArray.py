class BinaryTreeArray:
    def __init__(self, capacity):
        self.tree = [None] * capacity  # Array to store tree
        self.size = 0  # Current number of elements

    # Insert a node at the next available position
    def insert(self, key):
        if self.size >= len(self.tree):
            print("Tree is full")
            return
        self.tree[self.size] = key
        self.size += 1

    # Get left child index
    def left_child(self, index):
        left_index = 2 * index + 1
        return left_index if left_index < self.size else None

    # Get right child index
    def right_child(self, index):
        right_index = 2 * index + 2
        return right_index if right_index < self.size else None

    # Get parent index
    def parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    # Inorder traversal (recursive simulation)
    def inorder_traversal(self, index=0):
        if index is None or index >= self.size or self.tree[index] is None:
            return
        self.inorder_traversal(self.left_child(index))
        print(self.tree[index], end=" ")
        self.inorder_traversal(self.right_child(index))

    # Preorder traversal
    def preorder_traversal(self, index=0):
        if index is None or index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder_traversal(self.left_child(index))
        self.preorder_traversal(self.right_child(index))

    # Postorder traversal
    def postorder_traversal(self, index=0):
        if index is None or index >= self.size or self.tree[index] is None:
            return
        self.postorder_traversal(self.left_child(index))
        self.postorder_traversal(self.right_child(index))
        print(self.tree[index], end=" ")

    # Level Order Traversal
    def level_order_traversal(self):
        for i in range(self.size):
            if self.tree[i] is not None:
                print(self.tree[i], end=" ")
        print()

    # Search for a value in the tree
    def search(self, key):
        return key in self.tree

    # Delete a node (replace with last element)
    def delete(self, key):
        if key not in self.tree:
            print("Key not found")
            return
        index = self.tree.index(key)
        self.tree[index] = self.tree[self.size - 1]
        self.tree[self.size - 1] = None
        self.size -= 1


# Example Usage:
bt = BinaryTreeArray(10)  # Binary tree with capacity of 10 nodes
bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)
bt.insert(60)
bt.insert(70)

print("Inorder Traversal:")
bt.inorder_traversal()
print("\nPreorder Traversal:")
bt.preorder_traversal()
print("\nPostorder Traversal:")
bt.postorder_traversal()
print("\nLevel Order Traversal:")
bt.level_order_traversal()

# Search for a value
print("\nSearching for 30:", "Found" if bt.search(30) else "Not Found")

# Delete a node
bt.delete(30)
print("\nLevel Order Traversal after deleting 30:")
bt.level_order_traversal()
