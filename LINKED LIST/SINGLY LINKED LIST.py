class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertatend(self, d):
        newNode = Node()
        newNode.data = d
        newNode.next = None

        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def insertatbeg(self, d):
        newNode = Node()
        newNode.data = d
        newNode.next = self.head
        self.head = newNode

    def insertafter(self, d, x):
        newNode = Node()
        newNode.data = d
        newNode.next = None

        temp = self.head
        while temp.data != x:
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode

    def insertbefore(self, d, x):
        newNode = Node()
        newNode.data = d
        newNode.next = None

        prev = None
        temp = self.head

        while temp.data != x:
            prev = temp
            temp = temp.next

        newNode.next = temp
        if prev is not None:
            prev.next = newNode
        else:
            self.head = newNode   # if inserting before head

    def deleteatbeg(self):
        temp = self.head
        self.head = self.head.next
        temp = None

    def deleteatend(self):
        temp = self.head
        prev = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

    def deleteatmid(self, x):
        temp = self.head
        for i in range(1, x - 1):
            temp = temp.next

        temp.next = temp.next.next

    def search(self, d):
        temp = self.head
        while temp is not None:
            if temp.data == d:
                return 1
            temp = temp.next
        return 0

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            print(temp.next)
            temp = temp.next


List = LinkedList()
List.insertatend(10)
List.insertatend(20)
List.insertatend(30)
List.insertatbeg(40)
List.insertatbeg(50)
List.insertafter(60, 10)
List.insertbefore(70, 60)
List.deleteatbeg()
List.deleteatend()
List.deleteatmid(3)

List.display()

print("Node is Present" if List.search(60) == 1 else "Node is not Present")
