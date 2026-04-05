class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(list(set(nums)))

        res = 1
        local_res = 1

        for i in range(len(sorted_nums)-1):
            curr = sorted_nums[i]
            nex = sorted_nums[i+1]

            if nex-curr == 1:
                local_res += 1
                res = max(res, local_res)
            else:
                local_res = 1

        return res
