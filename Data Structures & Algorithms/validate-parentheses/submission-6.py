class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brace = "({["
        closed_brace = ")}]"

        for brace in s:
            if brace in open_brace:
                stack.append(brace)
            else:
                if len(stack):
                    o = stack.pop()
                    if ((brace == ")" and o != "(") 
                        or (brace == "}" and o != "{")
                        or (brace == "]" and o != "[")):
                            return False
                else:
                    return False

        return len(stack) == 0

           
           

