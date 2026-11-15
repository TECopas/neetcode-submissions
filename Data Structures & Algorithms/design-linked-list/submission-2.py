class ListNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.sentinel = ListNode()
        self.rearguard = ListNode()
        self.sentinel.next = self.rearguard
        self.rearguard.prev = self.sentinel
        self.size = 0

    def getIndex(self, index: int) -> ListNode:
        curIndex = 0
        curNode = self.sentinel.next
        while curIndex < index:
            curNode = curNode.next
            curIndex +=1
        return curNode

    def get(self, index: int) -> int:
        if index < 0 or index > self.size -1: #0 indexed, need the -1
            return -1
        retNode = self.getIndex(index)
        return retNode.val


    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.sentinel.next
        newNode.prev = self.sentinel
        self.sentinel.next.prev = newNode
        self.sentinel.next = newNode
        self.size +=1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.rearguard.prev
        newNode.next = self.rearguard
        self.rearguard.prev.next = newNode
        self.rearguard.prev = newNode
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == self.size:
            self.addAtTail(val)
            return

        workNode = self.getIndex(index)
        newNode = ListNode(val)

        newNode.next = workNode
        newNode.prev = workNode.prev
        workNode.prev.next = newNode
        workNode.prev = newNode
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        delNode = self.getIndex(index)

        delNode.prev.next = delNode.next
        delNode.next.prev = delNode.prev
        delNode.next = None
        delNode.prev = None
        self.size -=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)