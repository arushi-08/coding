class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1
        if n < 0:
            x = 1/x
            n = -n

        while n:
            if n & 1:
                res *= x
                n -= 1
            x = x*x
            n >>= 1
            
        return res

        """
        x=1/2, n=2
            res = 1/4
            n // 2 -> n = 1
        
        x=2, n=10
            res = 2*2 = 4
            n // 2 -> n = 5
            res = 4*2*2*2 = 32
            n // 2 -> n = 2
            res = 32*4 = 128
            n // 2 -> n = 1
            res = 128*4*2 = 1024
        
        """
