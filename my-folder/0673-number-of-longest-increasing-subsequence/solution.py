class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        

        dp = [1] * len(nums)
        ways = [1] * len(nums)

        for i in range(1, len(nums)):
            
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        ways[i] = ways[j]
                    elif dp[i] == dp[j] + 1:
                        ways[i] += ways[j]
        
        maxi = max(dp)
        count = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                count += ways[i]
        print(dp)
        print(ways)
        return count



