class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # return true if can reach last index
        # else return false

        # [2,3,1,1,4]

        # at each position take +pos[i]
        if len(nums) == 1: return True

        n = len(nums)
        goal = len(nums)-1

        for j in range(len(nums)-1,-1,-1):
            if nums[j] + j >= goal:
                goal = j

        return goal == 0

        # j=0
        # i=1 to 1 - no enter
        # 
