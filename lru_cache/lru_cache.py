import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
Our LRUCache class keeps track of the max number of nodes it
can hold, the current number of nodes it is holding, a doubly-
linked list that holds the key-value entries in the correct 
order, as well as a storage dict that provides fast access
to every node stored in the cache.
"""
class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  """
  Retrieves the value of the node given the key. Moves the
  retrieved node to the end of self.order. Should be an 
  O(1) operation.
  """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
            return node.value[1]
        else:
            return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  """
  Sets the given key-value pair as the new tail of self.order.
  Also adds the key-value pair to the self.storage. If 
  self.order is already holding the max number of pairs, the
  head of self.order will need to be evicted before the new
  key-value pair is added. Lastly, if the key already exists
  in the cache, the old value of the key should be updated, and
  the newly-updated key-value pair should then be moved to the
  end of self.order. Should be an O(1) operation.
  """
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
