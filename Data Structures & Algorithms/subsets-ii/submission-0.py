class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        sub = []

        def subsets(i):
            #print(i, sub)
            if i >= len(nums):
                ans.append(sub.copy())
                return

            # include nums[i]
            sub.append(nums[i])
            subsets(i+1)

            # exclude nums[i] --> If excluding; exclude all dups
            sub.pop()
            #print(i, sub)
            j = i
            while(nums[i]==nums[j]):
                j += 1
                if j == len(nums):
                    ans.append(sub.copy())
                    return 
            subsets(j)
        
        subsets(0)
        return ans