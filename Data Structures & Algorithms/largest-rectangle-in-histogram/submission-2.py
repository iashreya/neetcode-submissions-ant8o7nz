class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        nsr = [0]*len(heights)
        nsl = [0]*len(heights)

        # calculate next_smaller_right
        # array of indices
        # nsr[i] represents next smaller element to the right
        stack = []
        for i in range(len(heights)):
            while(stack and heights[stack[-1]] > heights[i]):
                nsr[stack.pop()] = i
            stack.append(i)

        for i in stack:
            nsr[i] = len(heights)

        # calculate next_smaller_left
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while(stack and heights[stack[-1]] > heights[i]):
                nsl[stack.pop()] = i
            stack.append(i)
        
        for i in stack:
            nsl[i] = -1


        # for each bar, calculate max area
        for i in range(len(heights)):
            width = nsr[i]-nsl[i]-1
            area = heights[i]*width
            ans = max(area, ans)

        return ans


