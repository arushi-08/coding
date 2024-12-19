class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # (i + n - 1)%n
        if len(nums)==1: return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):

        if not nums: return 0

        if len(nums)==1: return nums[0]

        prev2 = nums[0]
        prev = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            curr = max(prev, nums[i] + prev2)
            prev2 = prev
            prev = curr

        return prev
