class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        # -> str:
        # decimal

        # 333 | 4   | 0
        #       0
        #       40  | 0.0
        #       0
        #       400  | 0.01
        #       333
        #        670 | 0.01
        #      
        
        neg_sign = False
        if numerator * denominator < 0:
            neg_sign = True
            numerator = abs(numerator)
            denominator = abs(denominator)

        ans = str(numerator // denominator)
        if numerator % denominator == 0:
            if neg_sign:
                return '-'+ans
            return ans
        
        ans += '.'
        
        remainder = numerator % denominator
        seen = {}

        while remainder:
            numerator = remainder * 10
            remainder = numerator % denominator
            quotient = str(numerator // denominator)
            key = (quotient, remainder)

            if key in seen:
                result = ans[:seen[key]] + '(' + ans[seen[key]:] + ')'
                if neg_sign:
                    return '-'+result
                return result
            
            seen[(quotient, remainder)] = len(ans)
            ans += quotient

        if neg_sign:
            return '-'+ans
        return ans




