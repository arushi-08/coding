class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        # remove 3 smallest and largest elements
        # diff is somewhere there
        n = len(nums)
        if n <= 4:
            return 0
        
        nums.sort()

        return min(
            nums[n-1]-nums[3],
            nums[n-2]-nums[2],
            nums[n-3]-nums[1],
            nums[n-4]-nums[0]
        )
