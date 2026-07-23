class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {} # {target-nums[i]: i}

        for i in range(len(nums)):
            if h_map.get(nums[i]) != None:
                return [h_map.get(nums[i]), i]
            else:
                h_map[target-nums[i]] = i

        return[0,0]


