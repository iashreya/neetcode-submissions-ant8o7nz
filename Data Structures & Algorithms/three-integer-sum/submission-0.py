class Solution:
    def twoSum(self, nums, target):
        h_map = {}
        ans = []
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in h_map: 
               ans.append(sorted([-target, nums[i], target-nums[i]]))
            else:
                h_map[target-nums[i]] = i 
        return ans if len(ans)!=0 else None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            sums = self.twoSum(nums[:i]+nums[i+1:], -nums[i])
            if sums:
                for sum in sums:
                    if sum not in ans:
                        ans.append(sum)
        return ans