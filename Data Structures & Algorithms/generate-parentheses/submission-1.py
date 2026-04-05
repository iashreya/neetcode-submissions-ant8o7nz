class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.open_brace = 0 # open brace count
        self.closed_brace = 0 # closed brace count

        def create(s):
            print(s)
            if self.open_brace == self.closed_brace == n:
                ans.append(s)
                return

            if self.open_brace > n:
                return 

            # select a closed brach if there's an open brace
            if self.open_brace > self.closed_brace:
                self.closed_brace += 1
                create(s + ")")
                self.closed_brace -= 1

            # select open brace
            self.open_brace += 1
            create(s + "(")
            self.open_brace -= 1

        create("")
        return ans
                