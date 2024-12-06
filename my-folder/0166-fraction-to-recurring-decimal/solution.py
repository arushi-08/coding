class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # return fraction in string format

        # 0.012012012012
        # 0.011101110111 -> 0- 1-6
        # 0.011111111111

        if numerator % denominator == 0:
            return str(numerator // denominator)

        neg = False
        if numerator * denominator < 0:
            neg = True
            numerator = abs(numerator)
            denominator = abs(denominator)

        ans = str(numerator // denominator) + '.'
        
        numerator_quotient = []
        while True:
            remainder = numerator % denominator
            if remainder == 0:
                for n, q in numerator_quotient:
                    ans += str(q)
                break
            numerator = remainder * 10
            quotient = numerator // denominator
            
            if [numerator, quotient] in numerator_quotient:
                for n, q in numerator_quotient:
                    if [n,q] == [numerator, quotient]:
                        ans += '('
                    ans += str(q)
                ans += ')'
                break
            else:
                numerator_quotient.append([numerator, quotient])
        
        if neg:
            return '-' + ans
        return ans


