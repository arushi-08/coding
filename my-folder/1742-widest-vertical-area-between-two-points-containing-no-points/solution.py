class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        

        # just compare x axis

        points.sort(key=lambda x: x[0])
        maxwidth = 0
        for i in range(len(points)-1):
            maxwidth = max(maxwidth, points[i+1][0] - points[i][0])
        
        return maxwidth

