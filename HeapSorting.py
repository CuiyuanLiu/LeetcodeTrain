"""
https://blog.csdn.net/wtswts1232/article/details/139784189
"""

class Array(object):
    def __init__(self, size = 32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(self._size): self._items[i] = value

    def __iter__(self):
        for item in self._items: yield item
            
class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0
    
    # Function for shift up.
    def shiftup(self, nd_index):
        try:
            if (nd_index > 0):
                parent_index = int((nd_index - 1)/2)
                if (self._elements[parent_index] < self._elements[parent_index]):
                    self._elements[parent_index], self._elements[nd_index] = self._elements[nd_index], self._elements[parent_index]
                    self.shiftup[self._elements[parent_index]]
                else:
                    pass
        except Exception as err:
            print(err)
    
    # Function for shift down.
    def shiftdown(self, nd_index):
        try:
            left, right = 2 * nd_index + 1, 2 * nd_index + 2
            largest = left if (
                (left < self._count) and (self._elements[left] >= self._elements[right]) and (self._elements[left] >= self._elements[largest])
            ) else (
                right if ((right < self._count) and (self._elements[right] >= self._elements[largest])) else nd_index
            )
            if largest != nd_index:
                self._elements[largest], self._elements[nd_index] = self._elements[nd_index], self._elements[largest]

        except Exception as err:
            pass


import sys
lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == "": break
    lines.append(line)

lines[0]
