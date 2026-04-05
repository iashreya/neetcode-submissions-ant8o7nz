class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        current_product = 1

        for i in range(len(nums)):
            res[i] *= current_product
            for j in range(i+1, len(nums)):
                res[i] *= nums[j]
            current_product *= nums[i]


        return res