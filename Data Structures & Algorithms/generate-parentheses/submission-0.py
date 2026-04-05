class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def create(s, open_count, closed_count):
            if open_count == closed_count == n:
                ans.append(s)
                return

            if open_count > n or closed_count > n:
                return

            create(s + "(", open_count+1, closed_count)
            if open_count > closed_count:
                create(s + ")", open_count, closed_count+1)

        create("", 0, 0)
        return ans
                