class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while (l < r):
            flag = 0
            m = (l+r)//2

            if nums[l] > nums[m]:
                r = m
                flag = 1
            if nums[r] < nums[m]:
                l = m
                flag = 1
            if flag == 0 or (r-l)==1:
                break

        return min(nums[l], nums[r])