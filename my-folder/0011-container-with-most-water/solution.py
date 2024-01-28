class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxarea = 0
        currarea = 0
        i = 0
        j = len(height)-1
        while i < j:
            currarea=min(height[j], height[i])*abs(j - i)
            
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
            maxarea = max(maxarea, currarea)

        return maxarea
