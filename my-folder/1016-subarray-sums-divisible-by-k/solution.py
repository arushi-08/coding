class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # (p[j] - p[i])%k==0
        psum = 0
        hmap = {0:1}
        count = 0
        for i in range(len(nums)):
            psum += nums[i]
            psum %= k
            if psum in hmap:
                count += hmap[psum]
            hmap[psum] = hmap.get(psum, 0) + 1
    
        return count
        
