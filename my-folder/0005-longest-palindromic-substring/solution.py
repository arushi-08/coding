class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        dp = [[''] * len(s) for _ in range(len(s))]
        longest_pal_string = s[0]
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = s[i]
                    continue
                
                if s[i] == s[j] and (dp[i+1][j-1] or dp[i+1][j] == dp[i][j-1] != ''):
                    dp[i][j] = s[i] + dp[i+1][j-1] + s[j]
                    longest_pal_string = max(longest_pal_string, dp[i][j], key=len)

        return longest_pal_string
