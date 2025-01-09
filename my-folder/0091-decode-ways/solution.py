class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0]*(len(s)+1)
        dp[-1] = 1
        for idx in range(len(s)-1,-1,-1):
            for i in range(1,3):
                if idx + i > len(s) or s[idx] == '0': continue
                curr_digit = int(s[idx:idx+i])
                if 1 <= curr_digit <= 26:
                    dp[idx] += dp[idx+i]
        print(dp)
        return dp[0]
