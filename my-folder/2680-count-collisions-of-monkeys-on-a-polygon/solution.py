class Solution:
    def monkeyMove(self, n: int) -> int:
        
        # total ways of moves - no collision
        # 2**n - 2
        mod = 10**9+7
        return (pow(2,n, mod) - 2) % mod
