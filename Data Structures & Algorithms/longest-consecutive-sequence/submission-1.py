class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        ans, curr = 1, 1

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr += 1
            else:
                curr = 1

            ans = max(curr, ans) 

        return ans