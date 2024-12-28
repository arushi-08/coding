class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] = 1
                    continue
                
                if s[i] == s[j]:
                    dp[i][j] =  dp[i+1][j-1] + 2
                else:
                    t1 = 0
                    if i < len(s) - 1:
                        t1 = max(t1, dp[i+1][j])
                    if j > 0:
                        t1 = max(t1, dp[i][j-1])
                    if i < len(s) - 1 and j > 0:
                        t1 = max(t1, dp[i+1][j-1])
                    dp[i][j] = t1

        return dp[0][-1]
