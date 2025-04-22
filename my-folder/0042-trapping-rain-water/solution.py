class Solution:
    def trap(self, height: List[int]) -> int:
        """ 
        goal: max water trapped
        2 pointer problem

        We care about storing water at the pointers.
            compare l and r and see how much can be stored at l and r.


        no comparison of left_max and right_max with curernt step
            left_max and right max determine max water at left and right
            idea: compare left_

        """
        if len(height) <= 2 : return 0
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                # left wall is bottleneck, so we store water at left
                # and update left_max if curr height is greater
                water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
            
        return water


