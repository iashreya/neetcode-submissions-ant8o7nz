class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left+1 < right):
            mid = (left+right)//2

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return min(nums[left], nums[right])
