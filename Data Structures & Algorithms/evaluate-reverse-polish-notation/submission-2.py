class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ("+", "-", "*", "/"):
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(str(int(eval(val1 + i + val2))))
            else:
                stack.append(i)
            
        return int(stack.pop())