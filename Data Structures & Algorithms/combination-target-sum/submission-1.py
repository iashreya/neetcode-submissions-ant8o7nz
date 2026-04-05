class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.curr = []

        def dfs(i, total):
            if total == target:
                self.ans.append(self.curr.copy())
                return

            if i == len(nums) or total > target:
                return

            self.curr.append(nums[i])
            dfs(i, total + nums[i])
            self.curr.pop()
            dfs(i+1, total)

        
        dfs(0, 0)
        return self.ans