class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 1
        right = x
        
        while left < right:
            mid = (left+right)//2
            if mid*mid <= x:
                left = mid + 1
            else:
                right = mid - 1
            
        if left*left > x:
            return left - 1
        return left
