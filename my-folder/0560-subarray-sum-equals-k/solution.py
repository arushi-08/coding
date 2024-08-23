class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        [1,2,3-3,1,1,1,4,2,-3]
        |----|
        psum - k is the subarray sum from ((psum-k) to psum)
        as psum - psum - k = k
        hence, look for psum - k in hashmap
        '''
        psum = 0
        hmap = {0:1}
        ans = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum - k in hmap: # psum - k are the elements you exclude and you get subarray sum
                ans += hmap[psum - k]
            
            hmap[psum] = hmap.get(psum, 0) + 1 # {0:1,1:1,2:1}

        return ans
