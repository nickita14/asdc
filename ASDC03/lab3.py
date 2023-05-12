import csv

from binary_tree import BinarySearchTree
from binary_listed import DoublyLinkedList
from singly_listed import SinglyLinkedList


class Main:
    def __init__(self, column: int, list_of_elements: list):
        self.column = column
        self.list_of_elements = list_of_elements

    
if __name__ == "__main__":
    table_source = list(csv.reader(open('src/students.csv', "r"), delimiter=","))
    column_name = input(f"Enter the column ({', '.join(table_source[0])}): ")
    if type(column_name) != str or column_name not in table_source[0] or column_name.isdigit():
        print("Invalid column.")
        exit()
    column_index = table_source[0].index(column_name)

    if not table_source[1][column_index].isdigit():
        print("This column is not a number. Cannot sort it.")
        exit()
    
    column_to_list = [ int(row[column_index]) for row in table_source[1:] ]

    sort_field = Main(column_index, column_to_list)

    sll = SinglyLinkedList()
    dll = DoublyLinkedList()
    bst = BinarySearchTree()

    for element in sort_field.list_of_elements:
        sll.insert(element)
        dll.insert(element)
        bst.insert(element)
    
    # Singly Linked List operations
    print("Singly Linked List traversal:")
    sll.bypass_and_withdrawal()
    print(f"Searching for value 3 in Singly Linked List: {sll.search(3).data}")
    sll.remove(3)
    print("Singly Linked List traversal after removing 3:")
    sll.bypass_and_withdrawal()

    # Doubly Linked List operations
    print("Doubly Linked List traversal:")
    dll.bypass_and_withdrawal()
    print(f"Searching for value 3 in Doubly Linked List: {dll.search(3).data}")
    dll.remove(3)
    print("Doubly Linked List traversal after removing 3:")
    dll.bypass_and_withdrawal()

    # Binary Search Tree operations
    print(f"Binary Search Tree Inorder traversal: {bst.inorder_traversal()}")
    print(f"Searching for value 3 in Binary Search Tree: {bst.search(3).data}")
    bst.delete(3)
    print(f"Binary Search Tree Inorder traversal after removing 3: {bst.inorder_traversal()}\n")