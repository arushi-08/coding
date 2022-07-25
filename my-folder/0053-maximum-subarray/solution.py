class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum = float("-inf")
        maxsum = float("-inf")
        for i in range(len(nums)):
            currsum = max(currsum + nums[i], nums[i])
            maxsum = max(maxsum, currsum)
        
        return maxsum
