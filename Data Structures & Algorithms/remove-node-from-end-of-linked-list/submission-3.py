# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_count = 0
        node = head
        while(node):
            node_count += 1
            node = node.next

        prev = None
        node = head
        for i in range(node_count - n):
            prev = node
            node = node.next
        
        if node == head:
            head = head.next
            node.next = None
        else:
            prev.next = node.next
            node.next = None

        return head
