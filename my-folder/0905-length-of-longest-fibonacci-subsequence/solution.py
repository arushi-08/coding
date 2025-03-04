class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[2] * n for _ in range(n)]
        indexes = { n:i for i, n in enumerate(nums) }
        ans = 0
        for i in range(2, n):
            for j in range(i):
                k = indexes.get(nums[i] - nums[j], None)
                if k is not None and k < j:
                    dp[j][i] = dp[k][j] + 1
                    ans = max(ans, dp[j][i])
        
        if ans >= 3:
            return ans
        return 0
