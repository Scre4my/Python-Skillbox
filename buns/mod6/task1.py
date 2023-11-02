class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index):
        if self.head is None:
            raise IndexError("List is empty")
        current = self.head
        for _ in range(index):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        return current.data

    def remove(self, index):
        if self.head is None:
            raise IndexError("List is empty")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                if current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            if current.next is None:
                raise IndexError("Index out of range")
            current.next = current.next.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(n - 1):
                if current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

my_list = LinkedList()
my_list.push(10)
my_list.push(20)
my_list.push(30)
for item in my_list:
    print(item, end=" ")