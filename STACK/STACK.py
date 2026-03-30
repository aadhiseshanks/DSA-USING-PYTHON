class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, d):
        new_node = Node(d)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!!")
            return -1
        pop_value = self.top.data
        self.top = self.top.next
        return pop_value

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.top is None:
            print("Stack is Empty!!")
            return
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Main program
if __name__ == "__main__":
    size = int(input("Enter the Size of the Stack: "))

    s = Stack()

    print("Enter the Elements to Push:")
    for _ in range(size):
        data = int(input())
        s.push(data)

    print("Display the Stack:")
    s.display()

    val = int(input("If You want to Pop -> Press 1 Else Press 0: "))
    if val == 1:
        pops = int(input("Enter the Number of times Pop the Elements: "))
        for _ in range(pops):
            s.pop()

    print("Display the Stack:")
    s.display()
