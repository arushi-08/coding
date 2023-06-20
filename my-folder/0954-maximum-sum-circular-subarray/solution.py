class Solution:
    def getmaxsum(self, nums):
        currsum = 0
        maxsum = float('-inf')
        for i in range(len(nums)):
            if currsum + nums[i] > nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            maxsum = max(currsum, maxsum)
        return maxsum

    def getminsum(self, nums):
        currsum = 0
        minsum = float('inf')
        
        for i in range(len(nums)):
            if currsum + nums[i] < nums[i]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            minsum = min(currsum, minsum)
        return minsum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        max1 = self.getmaxsum(nums)
        totalsum = sum(nums)
        max2 = totalsum - self.getminsum(nums)
        return max(max1, max2) if max1 >=0 else max1


