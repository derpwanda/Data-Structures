class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node  # pointer


class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def insert():  # insert middle
        pass

    def insert_end(self, value):
        new_node = Node(value)
        self.tail.next_node = new_node  # change pointer
        self.tail = new_node
        # handle edge cases where linkedlist is 0

    def insert_begin(self, value):  # add before head
        new_node = Node(value)
        # establish the reference (now previous head)
        new_node.next_node = self.head
        self.head = new_node  # update head after pointing to previous head

    def find_length(self):
        # length = 0
        # current_node = self.head
        if self.head:
            length = 1  # start at 1
            current_node = self.head  # assign the current node
            while current_node.next_node:  # checks if next_node exists
                current_node = current_node.next_node
                length += 1  # add 1 to the length variable each time
            return length  # return the length number
        return 0

    # delete from any spot/middle
    def delete(self):
        pass

    # delete the head
    def delete_from_head(self):
        self.head = self.head.next_node
        # changes the designation of head to the next node

    # delete the tail
    def delete_from_tail(self, head, length):
        # change the pointer/next_node of the next to last node to None
        # we will need to traverse the entire node list to find the next to last # Node
        pass
