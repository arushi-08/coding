class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return -1

        maxdiff = -1
        stack = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= stack[-1]:
                stack.append(nums[i])
            else:
                maxdiff = max(maxdiff, stack[-1] - nums[i])

        return maxdiff


