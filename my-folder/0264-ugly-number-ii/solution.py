class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp = [0] * n
        dp[0] = 1

        head2, head3, head5 = 0,0,0

        for i in range(1,n):
            dp[i] = min(2*dp[head2], 3*dp[head3], 5*dp[head5])
            if dp[i] == 2*dp[head2]:
                head2+=1
            if dp[i] == 3*dp[head3]:
                head3+=1
            if dp[i] == 5*dp[head5]:
                head5+=1
            # print("dp[i]", dp[i], "head2", head2, "head3", head3, 'head5', head5, "dp", dp)
        return dp[n-1]
