class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        cursum = 0
        for num in nums:
            cursum += num
            # psum.append(cursum)
        # print(cursum)
        removed = 0
        for i in range(len(nums)):
            if cursum - nums[i] <= nums[i]:
                nums[i] == 0
                cursum -= nums[i]
                removed += 1
        
        return cursum if len(nums) - removed >= 3 else -1
