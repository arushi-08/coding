class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = float('-inf')
        st, ed = 0, 0
        currsum = 0
        while ed < len(nums):
            if nums[ed] < currsum + nums[ed]:
                currsum += nums[ed]
            else:
                currsum = nums[ed]
            # currsum = max(nums[ed], currsum+nums[ed])
            maxsum = max(maxsum, currsum)
            ed += 1
        return maxsum



