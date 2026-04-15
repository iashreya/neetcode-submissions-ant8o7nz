class Solution:
    def twoSum(self, nums, target, start):
        h_map = defaultdict(list)
        ans = []
        for i in range(start, len(nums)):
            if nums[i] in h_map:
                for _ in h_map[nums[i]]:
                    ans.append([_ , i])
            
            h_map[target-nums[i]].append(i)
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        for i in range(len(nums)):
            temp = self.twoSum(nums, -nums[i], i+1)
            print(temp)
            for j, k in temp:
                ans.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        
        return list(ans)

        