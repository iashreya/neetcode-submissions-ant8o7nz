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
            j = 0
            while node:
                heapq.heappush(heap, (node.val, i, j, node))
                node = node.next
                j += 1

        dummy = ListNode()
        node = dummy

        while(heap):
            val, i, j, temp = heapq.heappop(heap)
            node.next = temp
            node = temp
            temp.next = None

        return dummy.next