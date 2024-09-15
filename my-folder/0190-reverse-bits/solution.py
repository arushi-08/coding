class Solution:
    def reverseBits(self, n: int) -> int:
        
        reverse = 0
        j = 0
        for i in range(31, -1, -1):
            mask = 1 << i
            if (n & mask) != 0:
                set_mask = 1 << j
                reverse |= set_mask
            j += 1

        return reverse
