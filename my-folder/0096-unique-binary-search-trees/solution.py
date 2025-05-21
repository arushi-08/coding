class Solution:
    def __init__(self):
        self.memo = {}

    def numTrees(self, n: int) -> int:

        if n <= 2:  return n

        # if head = n
        # how many on left? 1 to n-1
        # how many on right? n+1 (not exist)

        ans = 0
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for j in range(3, n+1):
            for i in range(1, n+1):
                if j >= i:
                    dp[j] += max(1, dp[i-1]) * max(1, dp[j - i] )
            
        return dp[-1]


