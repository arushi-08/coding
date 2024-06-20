class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0: return '0'
        if num < 0:
            num = (1 << 32) + num
        
        hex_digits = '0123456789abcdef'
        ans = ''
        while num:
            rem = num % 16
            ans = hex_digits[rem] + ans
            num //= 16
        
        return ans

