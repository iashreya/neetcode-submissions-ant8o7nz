import math
import heapq
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, p in enumerate(points):
            x, y = p
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), i))
        
        ans = []
        for _ in range(k):
            dist, index = heapq.heappop(heap)
            ans.append(points[index])

        return ans