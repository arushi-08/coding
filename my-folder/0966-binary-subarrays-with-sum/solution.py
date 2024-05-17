class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum = 0
        cursum = 0
        hmap = {0:1}
        for i in range(len(nums)):
            psum += nums[i]
            elem = psum - goal
            if elem in hmap:
                cursum += hmap[elem]
            hmap[psum] = hmap.get(psum, 0) + 1
        
        return cursum
