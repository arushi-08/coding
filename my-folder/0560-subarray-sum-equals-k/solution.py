class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # psum
        # p[j] - k = p[i] - store in map
        hmap ={0:1}
        ans = 0
        psum = 0
        for j in range(len(nums)):
            psum += nums[j]
            if psum-k in hmap:
                ans += hmap[psum-k]
            hmap[psum] = hmap.get(psum, 0) + 1
        return ans

