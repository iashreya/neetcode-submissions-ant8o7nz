import math
import heapq
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, p in enumerate(points):
            x, y = p
            heapq.heappush(heap, ((x**2 + y**2), p))
        
        ans = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            ans.append(point)

        return ans