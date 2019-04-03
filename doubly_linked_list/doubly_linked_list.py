"""Each ListNode holds a reference to its previous node
    as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        # create a variable to manipulate self.prev of existing node
        current_prev = self.prev
        # point self.prev of existing node to a new ListNote
        self.prev = ListNode(value, current_prev, self)
        # if current_prev exists/is not None/there is something there now
        if current_prev:
            # current_prev.next is now the self.prev
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        """ if the head exists, apply the insert_before method on the head, then assign the self.head to the current self.head.prev """
        # if there is a head node
        if self.head:
            # apply the insertbefore method to head
            self.head.insert_before(value)
            # assign the new head
            self.head = self.head.prev
        # if there isn't a head node
        else:
            # assign head to a new List node
            self.head = ListNode(value)
            # make this singular node the tail as well
            self.tail = self.head

    def remove_from_head(self):
        pass
        """ if there is a head node, reassign the head variable to the next (head.next). Then delete the oldhead next pointer by reassigning to None.  """

    def add_to_tail(self, value):
        pass
        """ if self.head exists, apply the insert_after to the tail, then assign tail to the added node. If it doesn't exist (a singular node with a tail), create a new ListNode and assign head & tail to the new node """

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass
        # reassign pointers of node's prev/next
        # make node tail
        # then point old tail next to newtail
        # point new tail prev to old tail
        moved_node = node
        node.next.prev = node.prev
        # cut both connections first or cut one, move, then cut the other?
        self.tail.insert_after(moved_node)

    def delete(self, node):
        pass

    def get_max(self):
        pass
