class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def max(self, a, b):
        return a if a > b else b

    def get_height(self, root):
        if root is None:
            return -1
        return root.height

    def insert(self, data):
        self.root = self.insert_recursion(self.root, data)

    def insert_recursion(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert_recursion(root.left, data)
        elif data > root.data:
            root.right = self.insert_recursion(root.right, data)

        root.height = 1 + self.max(self.get_height(root.left),
                                   self.get_height(root.right))

        print(f"{root.data} Height is {root.height}")
        return root

    # Traversals
    def pre_order(self):
        self.pre_order_rec(self.root)
        print()

    def pre_order_rec(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order_rec(root.left)
            self.pre_order_rec(root.right)

    def in_order(self):
        self.in_order_rec(self.root)
        print()

    def in_order_rec(self, root):
        if root:
            self.in_order_rec(root.left)
            print(root.data, end=" ")
            self.in_order_rec(root.right)

    def post_order(self):
        self.post_order_rec(self.root)
        print()

    def post_order_rec(self, root):
        if root:
            self.post_order_rec(root.left)
            self.post_order_rec(root.right)
            print(root.data, end=" ")

    # Search
    def search(self, data):
        return self.search_rec(self.root, data)

    def search_rec(self, root, data):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self.search_rec(root.left, data)
        else:
            return self.search_rec(root.right, data)

    # Delete
    def delete(self, data):
        self.root = self.delete_rec(self.root, data)

    def delete_rec(self, root, data):
        if root is None:
            return None

        if data == root.data:
            # One or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Two children
            root.data = self.min_value(root.right)
            root.right = self.delete_rec(root.right, root.data)

        elif data < root.data:
            root.left = self.delete_rec(root.left, data)
        else:
            root.right = self.delete_rec(root.right, data)

        return root

    def min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.data


tree = BinaryTree()

size = int(input("Enter the Number of Nodes: "))
print("Enter the Elements:")

for _ in range(size):
    tree.insert(int(input()))

print("PreOrder Traversal:")
tree.pre_order()

print("InOrder Traversal:")
tree.in_order()

print("PostOrder Traversal:")
tree.post_order()

search_val = int(input("Enter the Search Data: "))
print(f"Searching for {search_val}: {tree.search(search_val)}")

val = int(input("If You Want to Delete a Node Press 1 Else Press 0: "))

if val == 1:
    times = int(input("Enter number of deletions: "))
    for _ in range(times):
        tree.delete(int(input("Enter value to delete: ")))

print("InOrder Traversal after deletion:")
tree.in_order()
