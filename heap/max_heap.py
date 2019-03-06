class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

    def delete(self):
        self.storage.remove()

    def get_max(self):
        if self.storage[0]:
            return self.storage[0]

    def get_size(self):
        return len(array)

    def _bubble_up(self, index):
        # parent = (index - 1)//2
        # while index > 1 and self.storage[parent(i)] < self.storage[i]
        pass

    def _sift_down(self, index):
        pass


array = [94, 77, 75, 43, 51, 48, 53, 29, 35, 26]
print(array)
print(f"length of array", len(array))
# print(array)
# print(len(array) - 1)
# print(array.index(26))  # 26
array.append(36)
print(array)
array.remove(36)
print(array)
print(array[0])  # should return 94
print(array[len(array)-1])  # returns the value at end of array
