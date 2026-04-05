# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while(curr and curr.val != 1001):
            curr.val = 1001
            curr = curr.next

        if curr:
            return True
        else:
            return False