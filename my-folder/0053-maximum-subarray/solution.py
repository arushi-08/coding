class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum = nums[0]
        maxsum = currsum
        start = 0
        for i in range(1, len(nums)):
            if currsum + nums[i] > nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            maxsum = max(maxsum, currsum)
        
        return max(maxsum, currsum)
        
