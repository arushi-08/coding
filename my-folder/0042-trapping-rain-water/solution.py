class Solution:
    def trap(self, height: List[int]) -> int:
        
        # track the max left height
        # track the max right height
        # max_right = float('inf')
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        #  _,0,1,1,2,2,2,2,3,3,3,3        <- max left
        #  _,0,1,0,2,2,1,0,3,2,1,2      <- max gap
        # get max_right also
        # max left > curr -> use min(max left, maxright) - curr
        # else 0

        # intuition the smaller of left and right walls determine the trapped water
        # use max_right as len(height)-1
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

