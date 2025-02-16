class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node in BST
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    # Search for a key in BST
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    # Inorder Traversal (Left -> Root -> Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    # Preorder Traversal (Root -> Left -> Right)
    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal (Left -> Right -> Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    # Level Order Traversal (BFS)
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.key, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Delete a node from BST
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return node

        # Searching for the node to delete
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with one or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children, replace with inorder successor
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_recursive(node.right, min_larger_node.key)

        return node

    # Find the smallest node (used for deletion)
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Recursive method to find the height of a node in BST
    def find_height(self, node):
        if not node:
            return -1  # Height of an empty subtree is -1
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return max(left_height, right_height) + 1


# Example Usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder(bst.root)
print("\nPreorder Traversal:")
bst.preorder(bst.root)
print("\nPostorder Traversal:")
bst.postorder(bst.root)
print("\nLevel Order Traversal:")
bst.level_order()

# Searching for a node
print("\n\nSearching for 40:", "Found" if bst.search(40) else "Not Found")
print("Searching for 100:", "Found" if bst.search(100) else "Not Found")

# Finding height of the root node
print("\nHeight of BST root:", bst.find_height(bst.root))

# Finding height of a specific node (e.g., node with key 30)
node_30 = bst.search(30)
print("Height of node 30:", bst.find_height(node_30) if node_30 else "Node not found")

# Deleting a node
bst.delete(30)
print("\nInorder Traversal after deleting 30:")
bst.inorder(bst.root)
