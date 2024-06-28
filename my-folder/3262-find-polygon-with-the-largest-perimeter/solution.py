class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        currsum = nums[0] + nums[1]
        perimeter = 0
        for i in range(2, len(nums)):
            if currsum > nums[i]:
                perimeter = currsum + nums[i]
            currsum += nums[i]

        if perimeter:
            return perimeter
        return -1
