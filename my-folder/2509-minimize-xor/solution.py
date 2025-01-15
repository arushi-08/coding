class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        # given 2 nums
        # find x:
        #   x has same num of set bits as num2 e.g. num2 has 2, x has 2 bits
        #   x xor num1 is minimal, i.e., x's set bits are same as num1 and num of bits is num2

        # num1 = 3 -  11
        # num2 = 5 - 101
        # ans = 3 -   11

        # count num of set bits in num2
        # starting with leftside, set 1 at same location as num1
        # for extra remaining bits, set them on right side
        L = len(bin(max(num1, num2))) - 2
        num2_set_bits = bin(num2).count('1')
        num1_bin_length_og = len(bin(num1))
        num1_bin = bin((num1 | 1 << L))[3:]
        print('num1_bin', num1_bin, 'num2_set_bits', num2_set_bits)
        min_xor = [0]*L
        for i, bit in enumerate(num1_bin):
            # if num1_bin is set at 2 i.e, 5 bits to left
            if not num2_set_bits:
                break
            if bit == '1':
                min_xor[i] = 1
                num2_set_bits -= 1
            else:
                min_xor[i] = 0
        
        i = len(min_xor)-1
        print(min_xor, i, num2_set_bits)
        while num2_set_bits:
            if min_xor[i] == 0:
                min_xor[i] = 1
                num2_set_bits -= 1
            i -= 1
        
        ans = 0
        for elem in min_xor:
            ans = (ans << 1) | elem
        
        return ans

            

