class Solution:
    def __init__(self):
#         nums = [1, 2, 3, 1]
#         memo = [1, 2, 4]
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        memo = [0] * (len(nums))
        
        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(memo[i-1], nums[i])
            else:
                memo[i] = max(memo[i-2] + nums[i], memo[i-1])
            # memo[i] = max(sum(list(range(0, i, 2))) + nums[i], sum(list(range(1, i, 2))))
            
        return memo[-1]
        
#         if not nums:
#             return 0
        
#         if len(nums) == 1:
#             return nums[0]
        
#         if len(nums) in self.memo:
#             return self.memo[len(nums)]
            
#         self.memo[len(nums)] = max(self.rob(nums[2:]) + nums[0], self.rob(nums[1:]))
        
#         return self.memo[len(nums)]
    
    
