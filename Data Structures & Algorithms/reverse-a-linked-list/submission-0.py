# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # 0 <- 1 <- 2 <- 3
        a = head # 0
        b = a.next # 1
        a.next = None

        while (b != None): # T
            c = b.next # 2 3 None
            b.next = a # 1 -> 0 2 -> 1 3 -> 2
            a = b      # a = 1, 2, 3
            b = c      # b = 2, 3, None

        return a
