class Solution:
    def findComplement(self, num: int) -> int:
        """
        xor with 1 flips the bit (note this is 1 bit we are talking about)
        xor with 0 gives the same bit
        """
        todo = num
        bit = 1
        while todo:
            num = num ^ bit
            bit = bit << 1
            todo = todo >> 1
        return num

