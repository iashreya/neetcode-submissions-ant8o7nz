# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointer and answer list l3
        t1 = l1
        t2 = l2
        l3 = ListNode((t1.val + t2.val)%10)
        t3 = l3

        # Calculate Initial Carry
        carry = 1 if t1.val+t2.val >= 10 else 0
        t1 = t1.next
        t2 = t2.next 
        
        # Calculate sum of each node while both t1 & t2 are not null
        while(t1 or t2):
            if t1 and t2:
                s = t1.val + t2.val + carry
                t = ListNode(s%10)
                t3.next = t
                carry = carry = s//10 if s >= 10 else 0
                t1 = t1.next
                t2 = t2.next
            elif t1:
                s = t1.val + carry
                t = ListNode(s%10)
                t3.next = t
                carry = carry = s//10 if s >= 10 else 0
                t1 = t1.next
            else:
                s = t2.val + carry
                t = ListNode(s%10)
                t3.next = t
                carry = carry = s//10 if s >= 10 else 0
                t2 = t2.next
            t3 = t3.next

        # A pending carry will result in a new node
        if carry:
            t = ListNode(carry)
            t3.next = t

        return l3