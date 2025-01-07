class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        
        # numerator -> dividend
        # denominator -> divisor
        if numerator % denominator == 0:
            return str(numerator//denominator)

        neg_sign = False
        if numerator < 0 and denominator < 0:
            pass
        elif numerator < 0 or denominator < 0:
            neg_sign = True
        
        dividend = abs(numerator)
        divisor = abs(denominator)

        # 4 / 333
        # 0.012
        # 400 -> 670 -> 4 -> 40

        ans = str(dividend//divisor) + '.'
        quotient, remainder = divmod(dividend, divisor)
        dividend = remainder * 10
        quotient_repeat_map = {}
        ans_idx = len(ans)

        while dividend:
            quotient, remainder = divmod(dividend, divisor)
            if remainder == 0:
                ans += str(quotient)
                if neg_sign:
                    return '-' + ans
                return ans
            
            if (quotient, remainder) in quotient_repeat_map:
                idx = quotient_repeat_map[(quotient, remainder)]
                ans = ans[:idx] + '(' + ans[idx:] + ')'
                if neg_sign:
                    return '-' + ans
                return ans
            
            ans += str(quotient)
            dividend = remainder * 10
            quotient_repeat_map[(quotient, remainder)] = ans_idx
            ans_idx += 1

        


