class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        currsum = 0
        start, end = 0, 0
        while end < len(nums):
            currsum += nums[end]
            while start <= end and currsum >= target:
                ans = min(ans, end - start + 1)
                currsum -= nums[start]
                start += 1
            end += 1

        if ans == len(nums)+1: return 0
        return ans

