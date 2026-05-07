# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n_lists = len(lists)
        heap = []

        for i in range(n_lists):
            node = lists[i]
            heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(-1001, None)
        node = dummy        

        while(any(heap)):
            val, i, temp = heapq.heappop(heap)
            if temp.next:
                heapq.heappush(heap, (temp.next.val, i, temp.next))
            node.next = temp
            node = temp
            node.next = None

        return dummy.next