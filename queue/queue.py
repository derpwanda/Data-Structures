
# array style
""" class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        self.size = len(self.storage)
        return self.size """


# linked list style
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
        # we will need to traverse the entire node list to find the next to last 
        # Node
        pass


class Queue():
    def __init__(self, head, tail):
        self.head = head
        self.size = 0
        # what data structure should we
        # use to store queue elements?

        # we will use a  since Queue is similar (but not the same) as Stack
        self.storage = LinkedList(head, tail)

    def enqueue(self, item):

        new_node = Node(item)
        current = self.storage.head

        if current is None:
            self.storage.head = new_node
            self.size += 1
        else:
            while current.next_node is not None:
                current = current.next_node
            self.storage.tail.next_node = new_node  # reassign oldtail pointer
            self.storage.tail = new_node  # reassign the tail

    def dequeue(self):
        # current = self.head
        # if current is not None:
        #     self.head = current.getNext()
        #     self.size -= 1
        # else:
        #     return None

        prev_head = self.storage.head
        self.storage.head = prev_head.next_node
        # head reference/pointer updated
        prev_head.next_node = None
        return prev_head  # the node we dequeued

    def len(self):
        return self.size

"""     def print_queue(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.value)
            current = current.next_node
        print(self.temp)

q = Queue(None, None)

q.enqueue("User01")
q.enqueue("User02")
q.enqueue("User03")
q.enqueue("User04")
q.enqueue("User05")

q.print_queue() """
