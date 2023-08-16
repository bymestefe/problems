"""
The question is:
Create a two dimensional array iterator class. The class must have next() and has_next() method.
The class will be initialized with array of arrays.
[[1, 2], [3], [], [4, 5, 6]] for this input --> the output is 1, 2, 3, 4, 5, 6
"""

class Iterator:
    
    def __init__(self, arrays):

        self.arrays = arrays
        self.column = 0
        self.row = 0
    
    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements in array")
        
        res = self.arrays[self.row][self.column]
        self.column += 1

        while self.row < len(self.arrays) and self.column >= len(self.arrays[self.row]):
            self.row += 1
            self.column = 0
        return res
    
    def has_next(self):
        return self.row < len(self.arrays) and self.column < len(self.arrays[self.row])
    

arrays = [[1, 2], [3], [], [4, 5, 6]]
iterator = Iterator(arrays)

while iterator.has_next():
    print(iterator.next())
    