class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix max & suffix max
        # curr water trapped = min(prefixmax, suffixmax) - height[i]
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0] = height[0]
        suffix_max[-1] = height[-1]

        for i in range(1, n):
            prefix_max[i] = max(height[i], prefix_max[i-1])
            suffix_max[n-1-i] = max(height[n-1-i], suffix_max[n-i])

        trapped_water = 0
        for i in range(len(height)):
            trapped_water += min(prefix_max[i], suffix_max[i]) - height[i]
        
        return trapped_water
