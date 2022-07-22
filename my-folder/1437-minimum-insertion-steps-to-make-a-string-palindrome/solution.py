class Solution:
    def minInsertions(self, s: str) -> int:
        
        s2 = list(s).copy()
        s2.reverse()
        s2 = "".join(s2)
        
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        pal_len = dp[n][n]
        # print(dp)
        return n-pal_len
                    
