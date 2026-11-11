# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #empty list edge case
        if head == None:
            return None

        #put the nodes into a stack, and then pop them into the new linked list
        stack = []

        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        #now that we have all of the nodes, 
        #we reassign their next pointers as we pop them into the stack
        head = stack.pop()
        cur = head
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        #assign the last node's next to none to end the list
        cur.next = None
        return head