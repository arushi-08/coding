class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n & 1:
            return 2*n
        
        return n
