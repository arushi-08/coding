class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # reasoning: power of 2 number has just 1 1-bit
        # and & (n-1) sets this 1 bit to 0
        return n > 0 and n & (n-1) == 0
            

