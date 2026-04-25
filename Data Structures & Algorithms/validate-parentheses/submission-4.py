class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brace = "({["
        closed_brace = ")}]"

        def is_match(open, closed):
            if open == "(" and closed == ")":
                return True
            if open == "{" and closed == "}":
                return True
            if open == "[" and closed == "]":
                return True

            return False

        for brace in s:
            if brace in open_brace:
                stack.append(brace)
            elif brace in closed_brace:
                if len(stack) == 0 or not is_match(stack.pop(), brace):
                    return False

        return len(stack) == 0

           
           

