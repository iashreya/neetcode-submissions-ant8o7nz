# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Let's go to the mid element
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None # End first node at None

        # Reverse second half
        prev, curr = None, head2
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head2 = prev

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


        

