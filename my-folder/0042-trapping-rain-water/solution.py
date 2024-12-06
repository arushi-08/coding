class Solution:
    def trap(self, height: List[int]) -> int:
        # i already saw prefix sum

        # compute how much water can be trapped

        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0,0,1,1,2,2,2,3,3,3,3,3]
        # [3,3,3,3,3,3,3,3,2,2,1,0]
        
        prefix_max = [0] * len(height)
        for i in range(1, len(height)):
            if height[i] < max(height[i-1], prefix_max[i-1]):
                prefix_max[i] = max(height[i-1], prefix_max[i-1])
        
        suffix_max = [0] * len(height)
        for i in range(len(height)-2,-1,-1):
            if height[i] < max(height[i+1], suffix_max[i+1]):
                suffix_max[i] = max(height[i+1], suffix_max[i+1])
        
        water = 0
        for i in range(len(height)):
            water += max(0, min(prefix_max[i], suffix_max[i]) - height[i])
        
        return water



