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
    def __init__(self, init_data=None, next_node=None):
        self.init_data = init_data
        self.next_node = next_node

    def getData(self):
        return self.init_data

    def getNext(self):
        return self.next_node

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_node):
        self.new_node = new_node


class Queue:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        # what data structure should we
        # use to store queue elements?

        # we will use a  since Queue is similar (but not the same) as Stack
        self.storage = []

    def enqueue(self, item):
        new_node = Node(item)
        current = self.head

        if current is None:
            self.head = new_node
            self.size += 1
        else:
            while current.getNext():
                    current = current.getNext()
                    self.size += 1
            current.setNext(new_node)

    def dequeue(self):
        current = self.head
        if current is not None:
            self.head = current.getNext()
            self.size += 1
        else:
            print("Queue is empty!")

    def len(self):
        return self.size
