class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        # compute prefixsum

        psum = {nums[0]: 0}
        prefixsum = nums[0]
        maxlength = 0
        if prefixsum == k:
            maxlength = 1

        for i in range(1, len(nums)):
            prefixsum += nums[i]
            if prefixsum == k:
                maxlength = max(maxlength, i+1)
            
            if prefixsum - k in psum:
                maxlength = max(maxlength, i - psum[prefixsum-k])

            if prefixsum not in psum:
                psum[prefixsum] = i

        return maxlength
        

        # for i in range(len(psum)):
        #     if 

