class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_maxsum = float("-inf")
        global_maxsum = float("-inf")
        curr_minsum = float("inf")
        global_minsum = float("inf")
        for i in range(len(nums)):
            curr_maxsum = max(curr_maxsum + nums[i], nums[i])
            global_maxsum = max(global_maxsum, curr_maxsum)
            curr_minsum = min(curr_minsum + nums[i], nums[i])
            global_minsum = min(global_minsum, curr_minsum)
        if global_maxsum > 0:
            return max(sum(nums)-global_minsum, global_maxsum)
        return global_maxsum
