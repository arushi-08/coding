class Solution:
    def __init__(self):
        self.memo = []
    def climbStairs(self, n: int) -> int:
        self.memo = [0]*(n + 1)
        return self.helper(n)
    
    def helper(self, n):
        if n in [0, 1]: return n
        if n == 2: return 2
        
        if self.memo[n] : return self.memo[n]
        self.memo[n] =  self.helper(n-1) + self.helper(n-2)
        return self.memo[n]
