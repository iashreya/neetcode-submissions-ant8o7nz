from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key in counter:
            heapq.heappush(heap, [counter[key], key])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for value, key in heap:
            ans.append(key)

        return ans