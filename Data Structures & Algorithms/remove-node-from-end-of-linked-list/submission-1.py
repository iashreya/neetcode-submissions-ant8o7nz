# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while(temp):
            count += 1
            temp = temp.next

        # Move prev to one node before the node to be deleted
        prev = head
        if (count-n-1) < 0:
            head = head.next

        for i in range(count-n-1):
            prev = prev.next

        curr = prev.next
        if curr:
            prev.next = curr.next
        else:
            prev = None

        return head
        
