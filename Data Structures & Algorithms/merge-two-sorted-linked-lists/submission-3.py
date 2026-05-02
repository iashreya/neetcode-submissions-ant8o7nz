# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p, c, list3 = None, None, None
        c1, c2 = list1, list2

        while(c1 and c2):
            if c1.val <= c2.val:
                c = c1
                c1 = c1.next
            else:
                c = c2
                c2 = c2.next

            if list3 is None:
                list3 = c
            else:
                p.next = c

            p = c
        
        temp = c1 if c1 else c2
        if p:
            p.next = temp
        else:
            list3 = temp
                    
        return list3


        