class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        seen = [False]*len(nums)

        def perms():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for j in range(len(nums)):
                if seen[j]:
                    continue

                perm.append(nums[j])
                seen[j] = True
                perms()
                perm.pop()
                seen[j] = False

        perms()
        return ans