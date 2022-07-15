class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = 1
        if n < 0: 
            x = 1/x
            n = -n
        while n > 0:
            if n % 2==1:
                result = result*x
            x = x*x
            n//=2
        return result
