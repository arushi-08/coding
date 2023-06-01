class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        # (tsum - (p[j]-p[i]) + p)%p = 0
        # (-tsum + p[j] + p)%p = p[i]%p
        tsum = sum(nums)
        if tsum % p == 0: return 0
        hmap = {0:-1}
        psum = 0 
        minsize = len(nums)
        for i in range(len(nums)):
            psum += nums[i]
            psum %= p
            diff = (psum - tsum + p)%p
            if diff in hmap:
                minsize = min(minsize, i - hmap[diff])
            hmap[psum] = i
        
        if minsize == len(nums): return -1
        return minsize


