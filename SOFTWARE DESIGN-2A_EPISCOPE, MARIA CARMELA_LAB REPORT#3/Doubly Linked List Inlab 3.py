#Doubly linked lisy
import gc

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, data):

        if prev_node is None:
            print("previous node cannot be null")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return

    def deleteNode(self, dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next is not None:
            dele.next.prev = dele.prev

        if dele.prev is not None:
            dele.prev.next = dele.next

        gc.collect()

    def display_list(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next

dll = DoublyLinkedList()

dll.insert_end(1)
dll.insert_front(2)
dll.insert_front(3)
dll.insert_end(9)
dll.insert_after(dll.head, 11)
dll.insert_after(dll.head.next, 15)

print("Linked Lists: ")
dll.display_list(dll.head)

print("\nAfter deleting an element: ")
dll.deleteNode(dll.head.next.next.next.next.next)

dll.display_list(dll.head)