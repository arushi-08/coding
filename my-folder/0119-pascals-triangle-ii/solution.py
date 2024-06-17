class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}
        def getnum(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            memo[(row, col)] = getnum(row-1, col-1) + getnum(row-1, col)
            return memo[(row, col)]

        ans = [0] * (rowIndex+1)
        for i in range(len(ans)):
            ans[i] = getnum(rowIndex, i)
        
        return ans
