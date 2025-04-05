class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0': return 0

        dp = [0] * (len(s)+1)
        dp[-1] = 1
        for i in range(len(dp)-2,-1,-1):
            # i=1,0
            if i <= len(s)-1: 
                if s[i] == '0':
                    dp[i] = 0
                else:
                    dp[i] += dp[i+1]
                    if i <= len(s)-2 and s[i:i+2] <= '26':
                        dp[i] += dp[i+2]
            
        return dp[0]
