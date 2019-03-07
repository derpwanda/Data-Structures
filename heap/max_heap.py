class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

    def delete(self):
        if self.storage:
            return self.storage.pop(0)

    def get_max(self):
        if self.storage[0]:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):    # index is given to us
        # after youve added to end of the heap and compare it up to the
        # correct position

        # if index == 0
        #   return (finished)
        # compare index to its parent
        # 1. if its Greater:
        #       swap with parent
        #       bubble_up(self, old_parent_index/new_index)
        # 2. if its LESS than
        #   return
        parent = (index - 1)//2
        left_child = (index * 2)+1
        right_child = (index * 2)+2
        #  ...
        # i = len(self.storage)-1
        heaplist = self.storage

        while heaplist[parent] < heaplist[index]:
            heaplist[index], heaplist[parent] = heaplist[parent], heaplist[index]
        

    def _sift_down(self, index):
        parent = (index - 1)//2
        left_child = (index * 2)+1
        right_child = (index * 2)+2
        # after removing root element, take final element in array
        # move it to beggining (root position) and compare to left and right
        # children

        #  1. if element has no children, STOP
        #  2. if element LESS than the max child
        #       swap with the max child
        #
        pass





arr = [94, 77, 75, 43, 51, 48, 53, 29, 35, 26]


array = []
print(array)
array.append(5)
array.append(6)
array.append(8)
array.append(10)
array.append(1)
array.append(2)
array.append(5)
array.append(7)
print(array)

n = len(array)


for i in array:
    if array[n//2] > arr[i]:
        arr[n//2], arr[i] = arr[i], arr[n//2]
    print(array)



# print(f"length of array", len(array))
# # print(array)
# # print(len(array) - 1)
# # print(array.index(26))  # 26
# array.append(36)
# print(array)
# array.remove(36)
# print(array)
# print(array[0])  # should return 94
# print(array[len(array)-1])  # returns the value at end of array
