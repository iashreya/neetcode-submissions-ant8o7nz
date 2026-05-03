# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes_count = 0
        node = head
        while(node):
            nodes_count += 1
            node = node.next

        mid = (nodes_count-1)//2  # mid = No. of times you move to next to reach the mid node.

        # Let's go to the mid element
        node = head
        for i in range(mid):
            node = node.next
        
        head2 = node.next 
        node.next = None # End first node at None

        # Reverse second half
        p = None
        c = head2
        if c:
            n = c.next
        while(c):
            c.next = p
            p = c
            c = n
            if n:
                n = n.next
        head2 = p

        # Merge first and second halves
        n1 = head
        n2 = head2

        while(n1 and n2):
            # Save n1.next and point it to n2
            t1 = n1.next
            n1.next = n2

            # Save n2.next and point it to t1
            t2 = n2.next
            n2.next = t1

            # Restore n1 and n2
            n1, n2 = t1, t2


        

