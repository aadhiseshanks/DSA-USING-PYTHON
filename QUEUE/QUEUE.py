class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty!!")
            return -1

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def display(self):
        if self.front is None:
            print("Queue is Empty!!")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Main logic
if __name__ == "__main__":
    size = int(input("Enter the Size of Queue: "))

    q = Queue()

    print("Enter the Elements to Queue: ")
    for _ in range(size):
        data = int(input())
        q.enqueue(data)

    print("Display the Queue: ")
    q.display()

    x = int(input("If You Want to Dequeue Press 1 Else Press 0: "))
    if x == 1:
        times = int(input("Enter the Times of Dequeue: "))
        for _ in range(times):
            q.dequeue()

    print("Display the Queue: ")
    q.display()
