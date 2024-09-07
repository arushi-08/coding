class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix sum
        if not nums:
            return 0
        
        psum = [nums[0]]
        for i in range(1, len(nums)):
            psum.append(psum[-1] + nums[i])

        hmap = {0:1}
        ans = 0
        for i in range(len(psum)):

            if psum[i] - k in hmap:
                ans += hmap[psum[i] - k]
            
            hmap[psum[i]] = hmap.get(psum[i], 0) + 1
        
        return ans

