class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        maxdiag = 0
        maxarea = 0
        for rect in dimensions:
            length, width = rect
            candidate_diag = length**2 + width**2
            if candidate_diag >= maxdiag:
                maxdiag = candidate_diag
        
        for rect in dimensions:
            length, width = rect
            if length**2 + width**2 == maxdiag:
                maxarea = max(maxarea, length*width)
        
        return maxarea
