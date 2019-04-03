class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node  # pointer


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, prev_node, value):  # insert middle
        # if the given prevnode does NOT EXIST
        if prev_node is None:
            print(f"The previous node provided does not exist")
            return
        else:
            # create the new node with the value
            new_node = Node(value)
            # reassign new_node's .next to the prevnode's next
            new_node.next = prev_node.next
            # reassign prevnode's next to the new_node
            prev_node.next = new_node

    def insert_end(self, value):
        # create new node
        new_node = Node(value)
        # if the list is empty, them make the newnode head
        if self.head is None:
            self.head = new_node
        else:
            # find the tail/final node in linkedlist
            # assign a variable (as to not change the actual head)
            last_node = self.head
            # traverse until arrive at tail == None
            # while .next has a value
            while last_node.next:
                # make last_node the next (ie, move down list)
                # see robot sort from sorting sprint
                last_node = last_node.next
            # when last_node.next has a value of None and 
            # falls out of the while loop, change the value
            # of next to the new node
            last.next = new_node
        
        # self.tail.next_node = new_node  # change pointer
        # self.tail = new_node
        # # handle edge cases where linkedlist is 0

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
        # changes the designation of head to the next node
        self.head = self.head.next_node

    # delete the tail
    def delete_from_tail(self, head, length):
        # change the pointer/next_node of the next to last node to None
        # we will need to traverse the entire node list to find the next to last # Node
        pass
