class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3, 2, 1, 2, 1]

        maxleft = height[0]
        maxright = height[-1]
        st, ed = 0, len(height)-1
        water = [0] * len(height)
        
        while st <= ed:

            if maxleft < maxright:
                water[st] = max(maxleft - height[st], 0)
                maxleft = max(maxleft, height[st])
                st += 1
            else:
                water[ed] = max(maxright - height[ed], 0)
                maxright = max(maxright, height[ed])
                ed -= 1

        return sum(water)
