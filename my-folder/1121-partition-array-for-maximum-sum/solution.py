class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # [1,4,1,5,7,3,6,1,9,9,3]
        # [1][7,7,7,7][9,9,9,9][9,3]
        # 1+7*4+9*4+9*2

        # we have k choices: 
        #   to include current element in j subarrays
        #    where 1 <= j <= k       [i-k,....i-1]
        
        dp = [0] * (len(arr)+1)

        for i in range(len(arr)+1):
            for j in range(1, k+1):
                if i - j >= 0:
                    dp[i] = max(dp[i],
                    dp[i-j] + max(arr[i-j:i])*j)
        
        return dp[-1]
