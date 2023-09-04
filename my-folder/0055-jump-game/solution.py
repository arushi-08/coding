class Solution:
    def __init__(self):
        self.memo = {}

    def canJump(self, nums: List[int]) -> bool:
        
        return self.helper(nums, 0)
    
    def helper(self, nums, start):
        if start in self.memo: return self.memo[start]
        if start >= len(nums)-1:
            return True

        ans = False
        for i in range(nums[start], 0, -1):
            ans = ans | self.helper(nums, start + i)
            if ans:
                break
        self.memo[start] = ans
        return ans
