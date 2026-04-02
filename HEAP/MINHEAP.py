class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = HeapNode(data)
            return
        
        self.recursiveInsert(data, self.root)

    def recursiveInsert(self, data, node):
        if node.left is None:
            node.left = HeapNode(data)
            self.heapify_up(node.left)
        elif node.right is None:
            node.right = HeapNode(data)
            self.heapify_up(node.right)
        else:
            if self.get_count(node.left) <= self.get_count(node.right):
                self.recursiveInsert(data, node.left)
            else:
                self.recursiveInsert(data, node.right)

    def get_count(self, node):
        if node is None:
            return 0
        return 1 + self.get_count(node.left) + self.get_count(node.right)

    def heapify_up(self, node):
        while node != self.root:
            parentNode = self.get_Parent(node, self.root)
            if parentNode and parentNode.data > node.data:
                parentNode.data, node.data = node.data, parentNode.data
                node = parentNode
            else:
                break

    def get_Parent(self, node, root):
        if root is None:
            return None
        
        if root.left == node or root.right == node:
            return root
        
        if root.left:
            parent = self.get_Parent(node, root.left)
            if parent: return parent

        if root.right:
            parent = self.get_Parent(node, root.right)
            if parent: return parent

        return None

    def extract_min(self):
        if self.root is None:
            print("Heap is Empty")
            return
        
        min_val = self.root.data
        last_node_value = self.remove_last_node()

        if last_node_value is not None:
            self.root.data = last_node_value
            self.heapify_down(self.root)   
        else:
            self.root = None               

        return min_val


    def remove_last_node(self):
        queue = [self.root]
        last_node = None

        while len(queue) != 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            last_node = current   

        if last_node:
            if last_node == self.root:
                return last_node.data
            
            parentNode = self.get_Parent(last_node, self.root)

            if parentNode.left == last_node:
                parentNode.left = None
            else:
                parentNode.right = None
            
            return last_node.data
        
        return None
    
    def heapify_down(self, node):
        while node:
            small = node

            if node.left and node.left.data < small.data:
                small = node.left

            if node.right and node.right.data < small.data:
                small = node.right

            if small != node:
                node.data, small.data = small.data, node.data
                node = small
            else:
                break


Heap = MinHeap()
Heap.insert(10)
Heap.insert(7)
Heap.insert(6)
Heap.insert(5)
Heap.insert(4)

print(Heap.extract_min())
