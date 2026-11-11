# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursive version
        #edge case for no list
        if not head:
            return None

        #build out the recursion to unfurl
        #assign to assure we have a head
        newHead = head
        #check if the next one exists
        if head.next:
            #begin the recursion
            newHead = self.reverseList(head.next)
            #assign head to the next next node to reverse the list
            head.next.next = head
        #assign head.next to none to make the tail, break link between nodes
        head.next = None
        
        return newHead