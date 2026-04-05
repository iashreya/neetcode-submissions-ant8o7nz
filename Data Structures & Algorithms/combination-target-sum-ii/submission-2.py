class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        chosen = []
        path = []

        def dfs(i, total):
            if total == target:
                chosen.append(path.copy())
                return

            if (i >= len(candidates) or total > target):
                return

            # include candidates[i]
            path.append(candidates[i])
            dfs(i+1, total+candidates[i])

            # exclude candidates[i]
            path.pop()
            j = i+1
            if j < len(candidates):
                while (candidates[i] == candidates[j]):
                    j += 1
                    if j == len(candidates):
                        return 
            dfs(j, total)

        dfs(0, 0)
        return chosen