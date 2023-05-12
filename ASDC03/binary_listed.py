class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            new_node = Node(data)
            curr.next = new_node
            new_node.prev = curr

    def search(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        return curr

    def remove(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = curr.next
            if curr.next:
                curr.next.prev = curr.prev

    def bypass_and_withdrawal(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        print()
