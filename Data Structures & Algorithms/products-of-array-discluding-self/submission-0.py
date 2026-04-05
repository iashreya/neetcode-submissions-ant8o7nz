class Solution:
    def count_zero(self, nums):
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        
        return count

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if self.count_zero(nums) > 1:
            return [0]*len(nums)
        if self.count_zero(nums) == 1:
            zero_pos = nums.index(0)
            product = 1
            for i in nums:
                if i != 0:
                    product *= i
            res = [0]*len(nums)
            res[zero_pos] = product
            return res
        
        product = 1
        for i in nums:
            product *= i
        
        return [product//i for i in nums]