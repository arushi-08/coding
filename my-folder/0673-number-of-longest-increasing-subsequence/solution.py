class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        cnt = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                
        max_lis_length = max(dp)
        num_lis = 0
        for i in range(len(dp)):
            if dp[i] == max_lis_length:
                num_lis += cnt[i]
        
        return num_lis
        
