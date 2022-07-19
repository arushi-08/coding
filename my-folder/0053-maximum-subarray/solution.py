class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum = float("-inf")
        maxsum = float("-inf")
        for i in range(len(nums)):
            if currsum + nums[i] < nums[i]:
                currsum = nums[i]
            else:
                currsum += nums[i]
            maxsum = max(currsum, maxsum)
        
        return maxsum
