class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        seen = [0]*len(nums)

        def perms():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for j in range(len(nums)):
                if not seen[j]:
                    perm.append(nums[j])
                    seen[j] = 1
                    perms()
                    perm.pop()
                    seen[j] -= 1

        perms()
        return ans