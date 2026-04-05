class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize variables
        i = 0
        j = len(nums)-1

        # binary search
        while(i <= j):
            mid = j+i//2
            
            if nums[mid] == target: # Found target; return index
                return mid
            elif nums[mid] < target: # Target to the right
                i = mid + 1
            else:                    # Target to the left
                j = mid - 1

        return -1