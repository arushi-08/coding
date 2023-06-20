class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum = nums[0]
        maxsum = currsum
        for i in range(1, len(nums)):
            if nums[i] + currsum > nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            maxsum = max(currsum, maxsum)
        
        return maxsum

