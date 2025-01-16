class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0]*(len(s)+1)
        dp[-1] = 1

        for idx in range(len(dp)-1,-1,-1):
            for i in range(1,3):
                if idx+i > len(s) or s[idx:idx+i] == '0':
                    break
                curr_word = s[idx:idx+i]
                if 0 <= int(curr_word) <= 26:
                    dp[idx] += dp[idx+i]

        return dp[0]
