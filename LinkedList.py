class Node:
    def __init__(self, data=None):
        self.data = data
        self.tail = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        data.tail = self.head
        self.head = data

    @property
    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.tail
        return count