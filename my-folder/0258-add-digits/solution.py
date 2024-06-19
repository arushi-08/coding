class Solution:
    def addDigits(self, num: int) -> int:
        
        ans = 0
        while num > 9:
            while num:
                ans += num % 10 
                num //= 10
            if ans > 9:
                num = ans
                ans = 0
        
        if ans:
            return ans
        return num
