from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        temp = list(counter.keys())
        temp.sort(key=lambda x:counter[x], reverse=True)
        return temp[:k]
