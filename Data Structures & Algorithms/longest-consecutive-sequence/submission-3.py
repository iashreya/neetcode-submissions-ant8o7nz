class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Step 1: Remove duplicates
        # Step 2: Sort nums
        nums = sorted(list(set(nums)))
        ans, curr = 1, 1

        # Step 3: Count consecutive sequence length; Reset if next_num > curr_num + 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                curr += 1
                ans = max(curr, ans) 
            else:
                curr = 1

        return ans