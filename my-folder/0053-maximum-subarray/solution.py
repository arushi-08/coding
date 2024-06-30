class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currsum = float('-inf')
        maxsum = float('-inf')

        for num in nums:
            currsum = max(currsum + num, num)
            maxsum = max(currsum, maxsum)
        
        return maxsum
