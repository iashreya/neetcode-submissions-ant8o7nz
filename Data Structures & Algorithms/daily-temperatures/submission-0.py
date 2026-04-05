class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(-1, 101)]
        res = defaultdict(int)

        for i, temp in enumerate(temperatures):
            if len(stack) != 0:
                idx_diff = 0
                top = stack[-1]
                while temp > top[1]:
                    idx_diff = i - top[0]
                    val = stack.pop()
                    res[val[0]] = idx_diff
                    top = stack[-1]

                stack.append((i, temp))
            else:
                stack.append((i, temp))

        return [res[i] for i in range(len(temperatures))]


