class Solution:
    def trap(self, height: List[int]) -> int:
        # calculate max_right
        # contains index j of largest height 
        # to the right from current idx i
        max_right = [0]*len(height)
        max_right[len(height)-1] = len(height)
        mx = len(height)-1
        for i in range(len(height)-1,-1,-1):
            if height[mx] <= height[i]:
                max_right[i] = mx
                mx = i
            else:
                max_right[i] = mx
        
        # calculate max_left
        # contains idx j of largest height
        # to the left from current idx i
        max_left = [0]*len(height)
        max_left[0] = -1
        mx = 0

        for i in range(1, len(height)):
            if height[mx] <= height[i]:
                max_left[i] = mx
                mx = i
            else:
                max_left[i] = mx

        #calculate area
        total_area = 0
        for i in range(1,len(height)-1):
            area = min(height[max_right[i]], height[max_left[i]]) - height[i]
            area = area if area > 0 else 0
            total_area += area

        return total_area



        
        