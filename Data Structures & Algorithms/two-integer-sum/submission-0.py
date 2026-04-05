class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {} # target - nums[i]: i
        for i in range(len(nums)):
            if h_map.get(nums[i]) is not None:
                return [h_map[nums[i]], i]

            h_map[target - nums[i]] = i

        return [-1,-1]
