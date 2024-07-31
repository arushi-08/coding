class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols+2) for _ in range(rows+1)]
        
        for j in range(1,rows+1):
            dp[j][0] = float('inf')
            dp[j][cols+1] = float('inf')
        
        # for j in range(col+1):
        #     dp[0][j] = float('inf')

        for j in range(1,rows+1):
            for k in range(1,cols+1):
                dp[j][k] = min(
                    dp[j-1][k-1],
                    dp[j-1][k],
                    dp[j-1][k+1]
                    ) + matrix[j-1][k-1]
        # print('dp', dp)
        ans = float('inf')
        for i in range(1, cols+1):
            ans = min(ans, dp[rows][i])
        return ans
    
    def helper(self, row, col, matrix):

        if row == len(matrix):
            return 0
        
        if col == len(matrix[0]) or col < 0:
            return float('inf')
        
        if (row,col) in self.memo:
            return self.memo[(row, col)]

        self.memo[(row, col)] = min(
            self.helper(row+1, col-1, matrix), 
            self.helper(row+1, col, matrix),
            self.helper(row+1, col+1, matrix)
        ) + matrix[row][col]

        return self.memo[(row, col)]
