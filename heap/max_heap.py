class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

        self._bubble_up(len(self.storage) - 1

    def delete(self):
        # if storage exists and is filled with something
        if self.storage:
            self.storage.pop(0)
        return
        # then i have to get the heap balanced again
        self._sift_down(self.storage)

    def get_max(self):
        # if storage exists and is filled with something
        if self.storage:
            self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):    # index is given to us
        # after youve added to end of the heap and compare it up to the
        # correct position
        # recursive
        # if index == 0
        #   return (finished)
        # compare index to its parent
        # 1. if its Greater:
        #       swap with parent
        #       bubble_up(self, old_parent_index/new_index)
        # 2. if its LESS than
        #   return
        parent=(index - 1)//2
        # left_child = (index * 2)+1
        # right_child = (index * 2)+2
        # print("before loop", self.storage)
        for i in range(len(self.storage) - 1):
            if index == 0:
                return
            else:
                while index > 0 and self.storage[parent] < self.storage[index]:
                    self.storage[index], self.storage[parent]=self.storage[parent], self.storage[index]

                    index=parent
                    parent=(index - 1)//2
        # print("after loop", self.storage)

    def _sift_down(self, index):
        parent=(index - 1)//2
        left_child=(index * 2)+1
        right_child=(index * 2)+2
        # after removing root element, take final element in array
        # move it to beggining (root position) and compare to left and right
        # children

        #  1. if element has no children, STOP
        #  2. if element LESS than the max child
        #       swap with the max child
        #
        pass


# arr = [94, 77, 75, 43, 51, 48, 53, 29, 35, 26]

# array = []
# print(array)
# array.append(5)
# array.append(6)
# array.append(8)
# array.append(10)
# array.append(1)
# array.append(2)
# array.append(5)
# array.append(7)
# print(array)

# n = len(array)

# for i in range(len(array)):
#     parent = (index - 1)//2
#     while index > 1 and array[parent] < array[index]:
#         array[parent], array[index] = array[index], array[parent]

# print(array)
