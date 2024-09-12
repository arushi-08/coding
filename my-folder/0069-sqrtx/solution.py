class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1: return 1
        ans = 0
        st = 1
        ed = x//2+1
        while st <= ed:
            mid = (st + ed) // 2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                ans = max(ans, mid)
                st = mid + 1
            else:
                ed = mid - 1
                
        
        return ans
