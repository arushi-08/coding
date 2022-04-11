# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int, start=1) -> int:
        
        if isBadVersion(start):
            return start
        left = start
        right = n
        ans = 0 
        while left <= right:
            
            mid = int(right + left)//2
            
            if isBadVersion(mid):
                ans = mid
                right = mid - 1
                # return self.firstBadVersion(mid, start)
            else:
                left = mid + 1
                # return self.firstBadVersion(n, mid)
        
        return ans
