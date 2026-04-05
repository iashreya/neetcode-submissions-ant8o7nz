class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        ans = []

        while(i < j):
            if numbers[i]+numbers[j] == target:
                ans.append([-target, numbers[i],numbers[j]])
                i += 1
                j -= 1
            if numbers[i]+numbers[j] > target:
                j -= 1
                continue
            if numbers[i]+numbers[j] < target:
                i += 1
                continue
        return ans if len(ans) > 0 else None


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            temp = self.twoSum(nums[i+1:],-nums[i])
            if temp:
                for t in temp:
                    if t not in ans:
                        ans.append(t)
        return ans

        