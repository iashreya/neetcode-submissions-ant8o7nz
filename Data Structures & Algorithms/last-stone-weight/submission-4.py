import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1*stone)

        while(len(heap) > 1):
            stone1 = -1*heapq.heappop(heap)
            stone2 = -1*heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, -1*(stone1-stone2))

        return -1*heap[0] if len(heap) > 0 else 0
