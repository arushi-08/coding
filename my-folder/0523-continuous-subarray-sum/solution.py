class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # psum 
        # calculate (p[j] - p[i]) % k == 0
        # p[j]%k = p[i]%k
        
        hmap = {0:-1}
        psum = 0
        for i in range(len(nums)):
            psum += nums[i] 
            psum %= k
            if psum in hmap and i - hmap[psum] >= 2:
                return True
            if psum in hmap:
                continue
            hmap[psum] = i
        return False
