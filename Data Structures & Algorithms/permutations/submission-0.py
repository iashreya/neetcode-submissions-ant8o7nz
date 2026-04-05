class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        self.perm = []

        def perms(i, seen):
            if i == len(nums):
                ans.append(self.perm.copy())
                return

            for j in range(len(nums)):
                if not seen.get(j):
                    self.perm.append(nums[j])
                    seen[j] = 1
                    perms(i+1, seen)
                    self.perm.pop()
                    seen.pop(j)

        perms(0, {})
        return ans