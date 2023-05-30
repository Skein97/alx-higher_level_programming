#!/usr/bin/python3

"""Define a class Node that defines a node of a singly linked list by:

    * Private instance attribute: data:
        ~ property def data(self): to retrieve it
        ~ property setter def data(self, value): to set it:
            - data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
    * Private instance attribute: next_node:
        ~ property def next_node(self): to retrieve it
        ~ property setter def next_node(self, value): to set it:
            - next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
    * Instantiation with data and next_node: def __init__(self, data, next_node=None):


And, define a class SinglyLinkedList that defines a singly linked list by:

    * Private instance attribute: head (no setter or getter)
    * Simple instantiation: def __init__(self):
    * Should be printable:
        ~ print the entire list in stdout
        ~ one node number by line
    * Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
"""


class Node:
    """Node class
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method to retrieve data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Method to set data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Method to retrieve next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Method to set next node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class
    """
    def __str__(self):
        """Private instance attribute head
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Method to initialize the SinglyLinkedList object
        """
        self.__head = None

    def sorted_insert(self, value):
        """Method to insert a new node into the correct sorted position in the list (increasing order) 
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
