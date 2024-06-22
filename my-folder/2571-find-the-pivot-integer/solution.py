class Solution:
    def pivotInteger(self, n: int) -> int:
    
        st = 1
        ed = n
        tsum = n*(n+1)//2
        while st <= ed:
            mid = (st+ed)//2
            psum = mid*(mid+1)//2
            nsum = tsum - psum + mid
            if psum == nsum:
                return mid
            if psum > nsum:
                ed = mid - 1
            else:
                st = mid + 1
        
        return -1


