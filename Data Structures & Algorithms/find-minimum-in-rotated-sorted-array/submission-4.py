class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left+1 < right):
            print(nums[left:right+1])
            mid = (left+right)//2

            # 3 4 5 6 1 2
            if nums[mid] > nums[left]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 4 5 0 1 2 3
                right = mid

        return min(nums[left], nums[right])
