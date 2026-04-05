# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2

        if t1 and t2:
            if t1.val <= t2.val:
                h = t1
                t1 = t1.next
            else:
                h = t2
                t2 = t2.next
        elif t1:
            return t1
        else:
            return t2

        t = h

        while (t1 or t2):
            if t1 and t2:
                if t1.val <= t2.val:
                    t.next = t1
                    t1 = t1.next
                else:
                    t.next = t2
                    t2 = t2.next
            elif t1 != None:
                t.next = t1
                t1 = t1.next
            else:
                t.next = t2
                t2 = t2.next
            
            t = t.next

        return h

        