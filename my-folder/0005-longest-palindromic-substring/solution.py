class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        n = len(s)
        dp = [[0]*(n) for _ in range(n)]
        max_len_pal = ''
        for i in range(n):
                dp[i][i] = True
                max_len_pal = s[i]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        
                        if len(s[i:j+1]) > len(max_len_pal):
                            max_len_pal = s[i:j+1]
        
        return max_len_pal
    
