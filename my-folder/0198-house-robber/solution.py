class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # self.memo = {}
        # return self.helper(nums, 0)

        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            for j in range(2,i+1):
                dp[i] = max(dp[i-j]+nums[i], dp[i])

        return max(dp)

    def helper(self, nums, index):

        if index >= len(nums):
            return 0

        if index in self.memo:
            return self.memo[index]

        self.memo[index] = max(self.helper(nums, index+2)+nums[index], self.helper(nums, index+1))

        return self.memo[index]
