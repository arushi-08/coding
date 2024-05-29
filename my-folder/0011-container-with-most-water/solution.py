class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        st = 0
        ed = len(height) - 1
        area = 0
        while st < ed:
            wdth = ed - st
            ht = min(height[st], height[ed])
            if wdth * ht > area:
                area = wdth * ht
            if height[st] > height[ed]:
                ed -= 1
            else:
                st += 1
        
        return area
