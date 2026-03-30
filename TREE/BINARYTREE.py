class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert level-order (same as array filling)
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Search element (BFS)
    def search(self, element):
        if self.root is None:
            return False

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.data == element:
                return True

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return False

    # Display (Level Order Traversal)
    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        print()

    # Get parent of a node
    def find_parent(self, value):
        if self.root is None or self.root.data == value:
            return None

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if (temp.left and temp.left.data == value) or \
               (temp.right and temp.right.data == value):
                return temp.data

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return None


# Main
if __name__ == "__main__":
    bt = BinaryTree()

    size = int(input("Enter number of nodes: "))
    print("Enter elements:")

    for _ in range(size):
        bt.insert(int(input()))

    print("Binary Tree (Level Order):")
    bt.display()

    # Root children
    if bt.root:
        print("Left Child of Root:", bt.root.left.data if bt.root.left else "None")
        print("Right Child of Root:", bt.root.right.data if bt.root.right else "None")

    # Parent
    value = int(input("Enter node to find parent: "))
    parent = bt.find_parent(value)
    print("Parent:", parent if parent is not None else "None")

    # Search
    element = int(input("Enter element to search: "))
    if bt.search(element):
        print(f"Element {element} present in the tree")
    else:
        print(f"Element {element} not present in the tree")
