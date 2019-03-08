class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)  # add value to last item of array
        self._bubble_up(len(self.storage) - 1)  # call the bubbleup last item in array

    def delete(self):
        # if storage exists and is filled with something
        if self.storage:
            root = self.storage[0]  # the value of storage[0] at this moment
            # make the value of root the value of the last item of array
            self.storage[0] = self.storage[len(self.storage) - 1]
            # removes the last item of array (ie, the old root)
            self.storage.pop()
            self._sift_down(0)  # call siftdown on the first element in array
            return root  #the original value of root

    def get_max(self):
        # if storage exists and is filled with something
        if self.storage:
            # return the first value in storage
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):    # index comes from insert()
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
        for i in range(len(self.storage) - 1):
            if index == 0:
                return
            else:
                while index > 0 and self.storage[parent] < self.storage[index]:
                    self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                    index = parent
                    parent = (index - 1)//2

    def _sift_down(self, index): # index comes from delete

        left_child = ((index * 2)+1)
        right_child = ((index * 2)+2)
        # _sift_down grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

        #  1. if index has no children, STOP
        #  2. if index LESS than the max child
        #       swap with the max child

        lenofarray = len(self.storage) - 1
        # print(index)
        # print(lenofarray)
        while index <= lenofarray:
            if ((index * 2)+1) <= lenofarray and ((index * 2)+2) <= lenofarray:
                if self.storage[(index * 2)+1] >= self.storage[(index * 2)+2]:
                    self.storage[(index * 2)+1], self.storage[index] = self.storage[index], self.storage[(index * 2)+1]
                    index = (index * 2)+1

                else:
                    self.storage[(index * 2)+2], self.storage[index] = self.storage[index], self.storage[(index * 2)+2]
                    index = (index * 2)+2

            elif ((index * 2)+1) <= lenofarray and self.storage[((index * 2)+1)] >= self.storage[index]:
                self.storage[(index * 2)+1], self.storage[index] = self.storage[index], self.storage[(index * 2)+1]
                index = (index * 2)+1

            elif ((index * 2)+2) <= lenofarray and self.storage[((index * 2)+2)] > self.storage[index]:
                self.storage[(index * 2)+2], self.storage[index] = self.storage[index], self.storage[(index * 2)+2]
                index = (index * 2)+2
            else:
                break
