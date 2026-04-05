class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h_map = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if numbers[i] in h_map:
                return [h_map[numbers[i]], i+1]
            else:
                h_map[diff] = i+1
        return [0,0]