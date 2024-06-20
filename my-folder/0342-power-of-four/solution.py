class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        return n > 0 and log(abs(n), 4) * 10 % 10 == 0
    
