class Solution:
    def trap(self, height: List[int]) -> int:
        

        prefix_max = [height[0]]
        for i in range(1, len(height)):
            prefix_max.append(max(prefix_max[-1], height[i]))
        
        # [0,1,1,2,2,2,2,3,3,3,3,3]
        # [3,3,3,3,3,3,3,3,2,2,2,1]
        # [0,1,0,2,1,0,1,3,2,1,2,1] - height
        # [0,0,1,0,1,2,1,] max(0,min(left, right) - height)

        suffix_max = [height[-1]]

        for i in range(len(height)-2,-1,-1):
            suffix_max.insert(0, max(suffix_max[0], height[i]))
        
        count = 0
        for i in range(len(height)):
            count += max(0, min(prefix_max[i], suffix_max[i]) - height[i])
        
        return count
