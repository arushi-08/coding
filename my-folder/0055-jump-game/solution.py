class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # when n <= 0 - return True
        # when n = 1 - [0] -> return False
        # when n = 1 - [>=1] -> return True
        # n = 2
        # return f(nums[i+step:]) | f(nums[i+step+1:])
        # time complexity: n*nums[i], i.e. 10^4 * 10^5
        
        if len(nums) == 1: 
            return True

        if nums.count(0) == 0:
            return True
        
        maxjump = 0

        for i in range(len(nums)):
            if maxjump < i:
                return False

            if maxjump >= len(nums)-1:
                return True
            
            maxjump = max(maxjump, i + nums[i])
        
        return False
