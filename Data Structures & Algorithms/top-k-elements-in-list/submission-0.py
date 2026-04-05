from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        res = sorted(freq.keys(), key=lambda x:freq[x], reverse=True)
        return res[:k]