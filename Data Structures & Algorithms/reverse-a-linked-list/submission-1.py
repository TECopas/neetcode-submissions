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
            #
            head.next.next = head
        head.next = None
        
        return newHead