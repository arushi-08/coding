class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        if not n:
            return 0
        # Since there are a lot more 2s than 5s in any n!, we just need to find the
        # number of 5s in n! and that will be the answer
        return n//5 + self.trailingZeroes(n//5)
    
