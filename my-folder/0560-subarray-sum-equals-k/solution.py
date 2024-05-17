from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        psumhmap = {0: 1}
        count = 0
        psum = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum - k in psumhmap:
                count += psumhmap[psum - k]
            psumhmap[psum] = psumhmap.get(psum, 0) + 1
        return count

