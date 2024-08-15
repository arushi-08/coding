class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [2,3,2]
        # base case
        #   [] -> return 0
        # max(rob(nums, idx+2)+currentamount, rob(nums, idx+1))
        if len(nums) == 1:
            return nums[0]
            
        memo = {}
        memo2 = {}
        return max(self.helper(nums[:-1], 0, memo),
        self.helper(nums, 1, memo2)
        )
    
    def helper(self, nums, idx, memo):

        if idx >= len(nums):
            return 0
        
        if idx in memo:
            return memo[idx]
        
        condn1 = self.helper(nums, idx+2, memo) + nums[idx]
        condn2 = self.helper(nums, idx+1, memo)

        memo[idx] = max(condn1, condn2)

        return memo[idx] 
