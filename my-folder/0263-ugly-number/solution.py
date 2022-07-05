class Solution:
    def isUgly(self, n: int) -> bool:
        
        for i in [2,3,5]:
            while n % i == 0:
                if n < i:
                    break
                n /= i
        
        if n == 1: return True
        return False
            
        
