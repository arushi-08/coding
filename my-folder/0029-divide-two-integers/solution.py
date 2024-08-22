class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # division methods - bit manipulation
        # bit right shift >> 1, but only with multiples of 2
        # dividend=24, divisor=3
        # 24 = 3 + 3 + 3 + 3 + 3 + 3 + 3 + 3 = 3 * 8
        #    = 3 * (2^3)

        # find max 2^num that can be subtracted from dividend
        # 10 - 2^3 = 2
        # 2 is less than 3 so we stop
        # add num to answer
        # repeat steps till div - 2^num < divisor

        sign = True # positive
        if dividend < 0 and divisor < 0:
            sign = True
        
        elif dividend < 0 or divisor < 0:
            sign = False
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while dividend >= divisor:

            num = 0

            while dividend >= divisor << (num + 1): # divisor * 2^(num+1)
                num += 1
            
            dividend -= divisor << num
            ans += 1 << num
        
        
        if ans >= 2**31 and not sign:
            return -2**31
        if ans >= 2**31:
            return 2**31-1

        if sign:
            return ans
        return ans * (-1)




