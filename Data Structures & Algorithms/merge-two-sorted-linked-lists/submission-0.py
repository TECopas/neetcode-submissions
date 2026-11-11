# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #need to traverse between both linked lists, adding nodes in the appropriate order
        head = None
        curL = None
        cur1 = list1
        cur2 = list2

        if cur1 == None:
            return cur2
        if cur2 == None:
            return cur1

        #get the head so we can assign curL appropriately
        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next

        curL = head

        #traverse the lists and add
        while cur1 is not None or cur2 is not None:
            if cur1 == None:
                curL.next = cur2
                cur2 = cur2.next
            elif cur2 == None:
                curL.next = cur1
                cur1 = cur1.next
            elif cur1.val <= cur2.val:
                curL.next = cur1
                cur1 = cur1.next
            else:
                curL.next = cur2
                cur2 = cur2.next
            curL = curL.next



        return head