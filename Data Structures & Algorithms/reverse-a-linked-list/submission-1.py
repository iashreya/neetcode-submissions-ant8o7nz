# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        p = None
        c = head
        n = c.next

        while(c != None):
            c.next = p
            p = c
            c = n
            if n:
                n = n.next

        head = p
        return head

