class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        subsetsum = totalsum / 2
        
        [1,5,11,5]
        [1] [5,11,5]    [] [5,11,5]
        [1,5] [11,5] [1] [11,5]    [5] [11,5] [] [11,5]
        
        recursive: idx, sum 
        
        """
        
        if sum(nums) % 2 == 1: return False
        
        subset_sum = sum(nums) // 2
        
        if subset_sum in nums: return True
        
        dp = [[False]*(subset_sum+1) for _ in range(len(nums))]
        dp[0][0] = True
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j == nums[i]:
                    dp[i][j] = True
                if j == 0 :
                    dp[i][j] = True
        
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                condn1 = False
                if nums[i] <= j:
                    condn1 = dp[i-1][j-nums[i]]
                condn2 = dp[i-1][j]
                
                dp[i][j] = condn1 or condn2
        
        return dp[len(nums)-1][subset_sum]
        
        
        
        
        
        
        
