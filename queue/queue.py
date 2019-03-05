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

'''
# linked list style
class QueueNode:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node
	
	def insert_node_begin(self, value):
		if not self.head

	def insert_node_end(self, value):
		pass
	
	def delete_node(self):
		pass

class Queue:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None
		self.storage = pass
	
	def __len__(self):
		return self.length

	def enqueue(self, item):
		if not self.head:
			new_node = Queue(value, None)
			self.head = new_node
			self.tail = new_node
		else:
			new_node = Queue(value, self.head)
			self.head = new_node
		self.size += 1
	
	def dequeue(self):
		pass
	
	def len(self):
		pass
'''