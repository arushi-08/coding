class Solution:
    def minInsertions(self, s: str) -> int:
        # LCS 
        
        s_reverse = list(s)
        s_reverse.reverse()
        s_reverse = "".join(s_reverse)
        
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == s_reverse[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return len(s) - dp[len(s)][len(s)]
