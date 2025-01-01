class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # n vertical lines drawn 2 endpoints of ith line are (i,0) (i,height[i])
        # find 2 lines that will hold max water

        maxarea = 0
        st = 0
        ed = len(height)-1
        while st < ed:
            maxarea = max(maxarea, min(height[st], height[ed]) * (ed-st))
            if height[st] < height[ed]:
                st += 1
            else:
                ed -= 1

        return maxarea
