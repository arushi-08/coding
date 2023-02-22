class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = float('-inf')
        currsum = float('-inf')
        for i in range(len(nums)):
            if nums[i] + currsum > nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]

            maxsum = max(maxsum, currsum)
        
        return maxsum
