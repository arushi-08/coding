class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(len(strs)):
            zeros = strs[i].count("0")
            ones = len(strs[i]) - zeros
            
            for j in range(m, zeros-1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones]+1)
            
        return dp[m][n]
                
