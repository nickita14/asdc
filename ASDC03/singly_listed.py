class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    # Search
    def search(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        return curr

    # Removal
    def remove(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
        else:
            curr = self.head
            while curr and curr.next and curr.next.data != data:
                curr = curr.next
            if curr and curr.next:
                curr.next = curr.next.next

    # Bypass and withdrawal
    def bypass_and_withdrawal(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        print()
