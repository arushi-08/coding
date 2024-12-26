class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maxsum = self.get_maxsum(nums)
        # use specialsum method
        right_max = self.get_right_max(nums)
        psum = 0
        special_sum = -float('inf')
        for i in range(len(nums)-1):
            psum += nums[i]
            special_sum = max(special_sum, psum + right_max[i+1])
        # print(right_max)
        return max(maxsum, special_sum)
    
    def get_maxsum(self, nums):
        currsum = -float('inf')
        maxsum = -float('inf')
        for i in range(len(nums)):
            currsum = max(currsum+nums[i], nums[i])
            maxsum = max(currsum, maxsum)
        return maxsum

    def get_right_max(self, nums):
        """array of max suffixsum from i to n-1"""
        ssum = nums[-1]
        right_max = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            ssum += nums[i]
            right_max.insert(0, max(right_max[0], ssum))
        
        return right_max
