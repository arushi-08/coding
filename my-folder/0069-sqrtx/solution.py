class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        
        l = 1
        r = x//2
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            
            if mid*mid == x:
                return mid
            
            if mid*mid < x:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return l - 1
