class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # return length of longest inc subseq
        # store min elem seen so far

        dp = [1]*len(nums)
        # store lis ending at index i

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

            

