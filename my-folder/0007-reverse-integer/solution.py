from math import log10, floor
class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0: return 0
        sign = x > 0
        x = abs(x)
        x_reverse = 0
        count = floor(log10(x))
        # x = 123
        # count = 2 | x_reverse += 300
        # count = 1 | x = 12 | x_reverse += 20
        # count = 0 | x = 1 | x_reverse += 1
        while x:
            quotient, remainder = divmod(x, 10)
            x_reverse += remainder * 10**count
            x = quotient
            count -= 1
        
        if sign:
            if x_reverse > (2**31)-1: 
                return 0
            return x_reverse
        
        if - x_reverse < -(2**31):
            return 0
        
        return -x_reverse
