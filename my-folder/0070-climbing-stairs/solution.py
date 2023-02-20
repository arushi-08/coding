class Solution:
    def __init__(self):
        self.dp = {}
    def climbStairs(self, n: int) -> int:
#       n steps total
#       each time climb once or twice
        # 1 + n-1 left   |.   2 + n-2 left
        if n in (0, 1, 2): 
            self.dp[n] = n
            return n
        if n < 0:  return 0

        if n in self.dp: return self.dp[n]

        self.dp[n] = (self.climbStairs(n-1) + 
        self.climbStairs(n-2))

        return self.dp[n]

