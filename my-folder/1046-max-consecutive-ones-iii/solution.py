class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window

        kcount = 0
        st = 0
        maxcount = 0
        
        for ed in range(len(nums)):
            
            if not nums[ed]:
                kcount += 1

            while kcount > k:
                if not nums[st]:
                    kcount -= 1
                st += 1
        
            maxcount = max(maxcount, ed - st + 1)
        
        return maxcount


