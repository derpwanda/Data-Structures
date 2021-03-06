# array style
class Queue:
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
        return self.size


# linked list style
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node  # pointer


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


class Queue():
    def __init__(self):
        # self.head = head
        self.size = 0
        # what data structure should we
        # use to store queue elements?

        # we will use a  since Queue is similar (but not the same) as Stack
        self.storage = LinkedList()

    def enqueue(self, item):

        new_node = Node(item)
        current = self.storage.head

        if current is None:
            self.storage.head = new_node
            self.storage.tail = new_node
            # self.storage.head.next_node = self.storage.tail
            self.size += 1
        else:
            self.storage.tail.next_node = new_node  # reassign oldtail pointer
            self.storage.tail = new_node  # reassign the tail
            self.size += 1

    def dequeue(self):

        if self.size > 1:
            temp = self.storage.head
            self.storage.head = temp.next_node
            # head reference/pointer updated
            temp.next_node = None
            self.size -= 1
            return temp.value  # the node we dequeued
        elif self.size == 1:
            current = self.storage.head
            self.storage.head = None
            self.storage.tail = None
            self.size -= 1
            return current.value
        else:
            return

    def len(self):
        return self.size

    def print_queue(self):
        current = self.storage.head
        self.temp = []
        while current:
            self.temp.append(current.value)
            current = current.next_node
        print(self.temp)

q = Queue()

print(f"after initializing empty q:", q.print_queue())

print(q.len())
q.enqueue("User01")
print(f"after adding a user:", q.len())
q.enqueue("User02")
q.enqueue("User03")
q.enqueue("User04")
q.enqueue("User05")
print(f"after adding 5 nodes:", q.print_queue())
print(f"size after add 5 nodes:", q.len())

q.dequeue()
print(f"list after a dequeue", q.print_queue())
