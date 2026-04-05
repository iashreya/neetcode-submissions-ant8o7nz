import math
import heapq
class Solution:
    def distance(self, p):
        x, y = p
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, p in enumerate(points):
            heapq.heappush(heap, (self.distance(p), i))
        
        ans = []
        for _ in range(k):
            dist, index = heapq.heappop(heap)
            ans.append(points[index])

        return ans