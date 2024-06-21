class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return '0'
        
        ans, n = '', abs(num)

        while n:
            n, remainder = divmod(n, 7)
            ans += str(remainder)
        
        if num < 0:
            ans += '-'
        
        return ans[::-1]

