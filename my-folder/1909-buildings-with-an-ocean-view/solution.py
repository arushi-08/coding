class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        maxht = -1
        indices = []
        for i in range(len(heights)-1, -1, -1):
            if maxht >= heights[i]:
                continue
            maxht = heights[i]
            indices.append(i)
        
        ans = []
        for i in range(len(indices)-1,-1,-1):
            ans.append(indices[i])
        return ans
