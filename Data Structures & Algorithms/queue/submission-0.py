class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.size = 0
        self.vanguard = Node()
        self.rearguard = Node()
        self.vanguard.next = self.rearguard
        self.rearguard.prev = self.vanguard

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new = Node(value)
        new.prev = self.rearguard.prev
        new.next = self.rearguard
        self.rearguard.prev.next = new
        self.rearguard.prev = new
        self.size += 1

    def appendleft(self, value: int) -> None:
        new = Node(value)
        new.prev = self.vanguard
        new.next = self.vanguard.next
        self.vanguard.next.prev = new
        self.vanguard.next = new
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        p = self.rearguard.prev
        self.rearguard.prev = p.prev
        p.prev.next = self.rearguard
        self.size -= 1
        return p.val 

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        p = self.vanguard.next
        self.vanguard.next = p.next
        p.next.prev = self.vanguard
        self.size -= 1
        return p.val 
