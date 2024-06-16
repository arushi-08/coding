class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        # check if any one rectangle is a line
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        
        # check if they don't overlap then rec1 is (LEFT or RIGHT or UP or DOWN) of rec2
        # overlap is negation of it.
        return not (rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3])
