"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):

        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1

        # check if the DLL is empty
        if self.head is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = self.head

        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's to previous to new node
            self.head.prev = new_node
            new_node.prev = None
            #set head to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        # store the value of the head
        # decrement the length of the DLL
        temp_head = self.head
        self.length -= 1
        # delete the head
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = self.head.next
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return temp_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):

        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # check if the DLL is empty
        if self.head is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):

        # store the value of the tail
        temp_tail = self.tail
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = self.tail.prev
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return temp_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        temp_node = node
        self.delete(node)
        self.add_to_head(temp_node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        temp_node = node
        self.delete(node)
        self.add_to_tail(temp_node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current_node = self.head
        max_value = None
        while current_node:
            if max_value is None or current_node.value > max_value.value:
                max_value = current_node
            current_node = current_node.next
        return max_value.value
