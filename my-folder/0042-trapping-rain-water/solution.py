class Solution:
    def trap(self, height: List[int]) -> int:

        maxleft, maxright = 0, 0
        left, right = 0, len(height)-1
        trapwater = 0
        while left < right:  

            if height[left] <= height[right]:
                maxleft = max(maxleft, height[left])
                trapwater += maxleft - height[left]
                left += 1
            else:
                maxright = max(maxright, height[right])
                trapwater += maxright - height[right]
                right -= 1
        
        return trapwater
        """
        ml = 0, mr = 1

        """

            


