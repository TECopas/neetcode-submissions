class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if self.arr[i] == 0: self.size+=1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: self.resize()
        self.arr[self.size] = n
        self.size+=1

    def popback(self) -> int:
        n = self.arr[self.size-1]
        self.arr[self.size-1] = 0
        self.size -=1
        return n

    def resize(self) -> None:
        self.capacity *=2
        newarr = [0] * self.capacity
        for i in range(len(self.arr)):
            newarr[i] = self.arr[i]
        self.arr = newarr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity