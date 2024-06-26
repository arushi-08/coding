# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        r, c = binaryMatrix.dimensions()

        rows = []
        for i in range(r):
            if binaryMatrix.get(i, c-1):
                rows.append(i)
        if not rows:
            return -1
        
        mincol = c-1
        for i in rows:
            st = 0
            ed = c-1
            while st < ed:
                mid = (st + ed) // 2

                if binaryMatrix.get(i, mid):
                    ed = mid
                else:
                    st = mid + 1
                
            mincol = min(mincol, ed)

        return mincol
