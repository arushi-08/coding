class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator== 0: return "0"
        if numerator%denominator == 0: return str(numerator//denominator)
        neg = False
            
        if numerator < 0 or denominator < 0:
            if not (numerator < 0 and denominator < 0):
                neg = True
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        ans = str(numerator//denominator) + '.'
        count = len(ans)-1

        dividend = numerator
        divisor = denominator
        visited = {}

        while dividend:
            quotient, remainder = divmod(dividend, divisor)
            if visited:
                ans += str(quotient)
                count += 1
                if dividend in visited and visited[dividend]>1:
                    idx = visited[dividend]
                    prefix = ''
                    if neg:
                        prefix = '-'
                    return prefix + ans[:idx] + '(' + ans[idx:-1] + ')'
            
            visited[dividend] = count
            
            if remainder == 0:
                break
            if remainder < divisor:
                dividend = remainder * 10

        if neg:
            return '-'+ans
        return ans

