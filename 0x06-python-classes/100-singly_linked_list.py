#!/usr/bin/python3
""" defines a node of a singly lineked list """
class Node:
    """ Defines a node of a singly linked list. """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): The next node in the list.
            Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the data stored in the node. """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to store in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieves the next node. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node:

        Args:
            value (NOde): The next node in the list.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list. """

    def __init__(self):
        """ Initializes a new SinglyLinkedList instance. """
        self.__head = None

    def __str__(self):
        """ Defines the string representation of the list. """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
        list (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is \
                    not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
