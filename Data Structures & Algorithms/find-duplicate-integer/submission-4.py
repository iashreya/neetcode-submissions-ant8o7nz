from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1, 3, 4, 2, 2
        for i in range(len(nums)):
            curr = abs(nums[i])
            # print(curr, nums)
            if nums[curr-1] < 0: 
                return curr
            nums[abs(curr)-1] *= -1
        return -1 