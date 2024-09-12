class Solution:
    def reverse(self, x: int) -> int:
        
        sign = True # positive
        if x < 0:
            sign = False

        x = abs(x)

        new_x = 0
        while x:
            new_x *= 10
            new_x += (x % 10)
            x //= 10
        
        if new_x >= 2**31 and sign:
            return 0
        
        if new_x > 2**31 and not sign:
            return 0

        if not sign:
            return -new_x
        return new_x
