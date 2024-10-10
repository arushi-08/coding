class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        stack = []
        ans = 0

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        for i in range(len(nums))[::-1]:
            while stack and nums[i] >= nums[stack[-1]]:
                ans = max(ans, i - stack[-1])
                stack.pop()

        return ans
            
