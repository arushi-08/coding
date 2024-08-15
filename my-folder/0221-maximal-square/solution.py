class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # find largest squares

        dp = [[0] * (len(matrix[0])) for _ in range(len(matrix))]

        side = 0

        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                side = 1
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                side = 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
                side = max(side, dp[i][j])
        # print('dp', dp)
        return side * side
