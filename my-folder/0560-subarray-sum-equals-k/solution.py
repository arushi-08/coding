class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # num of subarr with sum k
        hmap = {}
        hmap[0] = 1
        psum = 0
        ans = 0
        for num in nums:
            psum += num
            if psum - k in hmap:
                ans += hmap[psum-k]
            hmap[psum] = hmap.get(psum, 0) + 1

        return ans



