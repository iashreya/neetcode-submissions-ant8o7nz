class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(num, curr+num)
            ans = max(curr, ans)

        return ans