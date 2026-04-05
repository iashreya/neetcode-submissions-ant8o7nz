class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            area = heights[i]
            smallest_bar = heights[i]
            for j in range(i+1, len(heights)):
                smallest_bar = min(smallest_bar, heights[j])
                temp_area = smallest_bar * (j-i+1)
                area = max(temp_area, area)
            ans = max(area, ans)
        return ans