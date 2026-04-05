import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for i in nums:
            heapq.heappush(self.nums, i)
        
        req = len(nums)-k
        for _ in range(req):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
