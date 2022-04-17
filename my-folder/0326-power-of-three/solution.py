
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n==1:
            return True
        if n%3!=0:
            return False
        
        for i in range(n):
            
            if pow(3, i) == n:
                return True
            if pow(3, i) > n:
                return False
        
        return False
