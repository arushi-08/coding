class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        if nums.count(0) == 0:
            return True

        max_jump = nums[0]
        for i in range(len(nums)):
            
            if max_jump < i:
                return False

            max_jump = max(max_jump, i + nums[i])
            # print('max_jump', max_jump)
            if max_jump >= len(nums):
                return True
        
        return True
