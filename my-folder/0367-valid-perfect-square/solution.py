class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2: return True

        st = 0
        ed = num//2 + 1
        while st < ed:
            mid = (st + ed) // 2
            ans = mid * mid
            if ans == num:
                return True
            if ans > num:
                ed = mid
            else:
                st = mid + 1

        return False
