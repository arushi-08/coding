class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c == 0: return True

        st = 0
        ed = int(c**0.5)
        while st <= ed:
            if st**2 + ed ** 2 == c:
                return True
            if  st**2 + ed ** 2 > c:
                ed -= 1
            else:
                st += 1
            
        return False
