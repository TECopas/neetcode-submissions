class LinkedList:
    
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        count = 0
        node = self.head
        while count != index:
            if node == None: return -1
            node = node.next
            count +=1
        return node.val

    def insertHead(self, val: int) -> None:
        newNode = self.ListNode(val)
        newNode.next = self.head
        self.head = newNode
        if self.size == 0: self.tail = newNode
        self.size+=1

    def insertTail(self, val: int) -> None:
        newNode = self.ListNode(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size+=1

    def remove(self, index: int) -> bool:
        #4 cases, removing head, removing btwn head and tail, removing tail, and invalid index
        #invalid index
        if index >= self.size: return False
        #removing head
        if index == 0: 
            self.head = self.head.next
            if not self.head: self.tail = None
        else:
            #removing btwn head and tail
            curr = self.head
            for _ in range(index -1): curr = curr.next
            target = curr.next 
            curr.next = target.next
            #removing tail
            if not curr.next: self.tail = curr
        self.size -=1
        return True

    def getValues(self) -> List[int]:
        arr = []*self.size
        node = self.head
        while node != None:
            arr.append(node.val)
            node = node.next
        return arr 
