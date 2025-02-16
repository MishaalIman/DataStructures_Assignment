class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)

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

    # Level Order Traversal (Breadth-First Search)
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

    # Insert a node at the first empty place in level order
    def insert(self, key):
        new_node = Node(key)
        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Delete a node from Binary Tree
    def delete(self, key):
        if not self.root:
            return None

        queue = [self.root]
        key_node = None
        last_node = None

        # Find the node to delete and track the last node
        while queue:
            last_node = queue.pop(0)

            if last_node.key == key:
                key_node = last_node

            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        # Replace key_node's value with last_node's value and delete last node
        if key_node:
            key_node.key = last_node.key
            self._delete_deepest(last_node)
            print(f"Deleted {key} from the tree.")
        else:
            print(f"Node {key} not found.")

    # Helper function to delete the deepest node
    def _delete_deepest(self, delete_node):
        queue = [self.root]
        while queue:
            temp = queue.pop(0)

            if temp is delete_node:
                temp = None
                return

            if temp.right:
                if temp.right is delete_node:
                    temp.right = None
                    return
                queue.append(temp.right)

            if temp.left:
                if temp.left is delete_node:
                    temp.left = None
                    return
                queue.append(temp.left)


# Example Usage:
bt = BinaryTree(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(6)
bt.insert(7)

print("Inorder Traversal:")
bt.inorder(bt.root)
print("\nPreorder Traversal:")
bt.preorder(bt.root)
print("\nPostorder Traversal:")
bt.postorder(bt.root)
print("\nLevel Order Traversal:")
bt.level_order()

# Deleting a node
bt.delete(3)
print("\nLevel Order Traversal after deleting 3:")
bt.level_order()
