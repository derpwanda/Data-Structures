class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        # if storage exists and is filled with something
        if self.storage:
            root = self.storage[0]
            self.storage[0] = self.storage[len(self.storage) - 1]
            self.storage.pop()
            self._sift_down(0)  # call siftdown on the first element in array
            return root
        #print(f"delete", self.storage.pop(0))
        # then i have to get the heap balanced again
        #print(len(self.storage)-1)

    def get_max(self):
        # if storage exists and is filled with something
        if self.storage:
            return self.storage[0]

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
        parent = (index - 1)//2

        # print("before loop", self.storage)
        for i in range(len(self.storage) - 1):
            if index == 0:
                return
            else:
                while index > 0 and self.storage[parent] < self.storage[index]:
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                    index = parent
                    parent = (index - 1)//2
         # print("after loop", self.storage)

    def _sift_down(self, index):
        parent = (index - 1)//2
        left_child = ((index * 2)+1)
        right_child = ((index * 2)+2)
        # _sift_down grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

        #  1. if index has no children, STOP
        #  2. if index LESS than the max child
        #       swap with the max child

        lenofarray = len(self.storage) - 1
        print(index)
        print(lenofarray)
        while index < lenofarray:    
            if left_child < lenofarray and ((index * 2)+2) < lenofarray:
                if self.storage[(index * 2)+1] > self.storage[(index * 2)+2]:
                    self.storage[(index * 2)+1], self.storage[index] = self.storage[index], self.storage[(index * 2)+1]
                    index = (index * 2)+1

                else:
                    self.storage[(index * 2)+2], self.storage[index] = self.storage[index], self.storage[(index * 2)+2]
                    index = (index * 2)+2

            elif ((index * 2)+1) < lenofarray and self.storage[((index * 2)+1)] > self.storage[index]:
                self.storage[(index * 2)+1], self.storage[index] = self.storage[index], self.storage[(index * 2)+1]
                index = (index * 2)+1

            elif ((index * 2)+2) < lenofarray and self.storage[((index * 2)+2)] > self.storage[index]:
                self.storage[(index * 2)+2], self.storage[index] = self.storage[index], self.storage[(index * 2)+2]
                index = (index * 2)+2
            else:
                break


        # if (index * 2)+1 exists and right_child exist:
        #   if left > right:
        #   use left
        #   otherwise use right
        # if right_side exists
        #   and is larger than index
        #   swap
        # if left_child exists
        #   and is larger than index
        #   swap


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
