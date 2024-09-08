class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        if nums.count(0) == 0:
            return True
            
        maxjump = 0

        for i in range(len(nums)):
            if maxjump < i:
                return False
            
            if maxjump > len(nums)-1:
                return True
            
            maxjump = max(maxjump, i + nums[i])
        
        return True
