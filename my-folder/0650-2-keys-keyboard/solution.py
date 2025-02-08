class Solution:
    def minSteps(self, n: int) -> int:
        
        if n == 1: return 0

        d = 2
        res = 0
        while n > 1:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        
        return res
