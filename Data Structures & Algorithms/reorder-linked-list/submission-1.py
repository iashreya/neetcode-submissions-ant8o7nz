# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        count = 0
        while(temp):
            count += 1
            temp = temp.next

        # Find end of first half
        mid_node = head
        for i in range((count-1)//2):
            mid_node = mid_node.next

        # Reverse the second half
        prev = None
        curr = mid_node.next
        mid_node.next = None
        while(curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge both halves
        x, y = head, prev
        while(x and y):
            x_next = x.next
            y_next = y.next
            x.next = y
            if x_next:
                y.next = x_next
            x = x_next
            y = y_next
