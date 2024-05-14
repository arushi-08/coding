class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxarea = 0
        stack = [(-1,-1)]

        for i in range(len(heights)):
            while stack[-1][0] >= heights[i] and stack[-1][1] != -1:
                currht, curridx = stack.pop()
                area = currht * (i - 1 - stack[-1][1])
                maxarea = max(maxarea, area)
            stack.append((heights[i], i))

        while stack[-1][1] != -1:
            currht, curridx = stack.pop()
            area = currht * (len(heights) - 1 - stack[-1][1])
            maxarea = max(maxarea, area)
        
        return maxarea
                
            
