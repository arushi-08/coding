class Solution:
    def __init__(self):
        self.memo = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*(n+1)]*(m+1)
        
        for i in range(m + 1):
            for j in range(n + 1):
                    
                if i < 1 or j < 1:
                    continue
                    
                elif i == 1 or j == 1:
                    dp[i][j] = 1
                    
                elif i == j and i == 2:
                    dp[i][j] = 2
                    
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # print(dp, m-1, n)
        # dp[m][n] = dp[m-1][n] + dp[m][n-1]       
        
        return dp[m][n]
        
        
#         if m == n and m < 1:
#             return 0
        
#         if m != n and (m < 1 or n < 1):
#             return 0
        
#         if m == 1 or n == 1:
#             return 1
        
#         if m == n and m == 2:
#             return 2
        
#         if (m,n) in self.memo:
#             return self.memo[(m,n)]
        
#         self.memo[(m,n)] =  self.uniquePaths(m - 1, n) + self.uniquePaths(m, n-1)
#         return self.memo[(m,n)]
    
