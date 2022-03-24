from multiprocessing import Value


class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self): 
      self.head = None

    def append(self, vlaue):
        new_node = Node(Value)

        if self.head is None:
            self.head = new_node 
            print("Head Node created:", self.head.value)
            return


            # Identifying the tail node #
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node 
        print("Append new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
