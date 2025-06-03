class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        # [1,8,6,2,5,4,8,3,7]
        """
        2 pointer: st=0, ed=len(height)-1
        move smaller height[ptr] ptr forward/backward
        """

        maxarearesult = 0
        st = 0 
        ed = len(height)-1

        while st < ed:
            maxarearesult = max(maxarearesult, (ed-st)* min(height[st], height[ed]) )
            if height[st] <= height[ed]:
                st += 1
            else:
                ed -= 1
        
        return maxarearesult



