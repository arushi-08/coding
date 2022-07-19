class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ptr1 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[ptr1] = nums[ptr1], nums[i]
                ptr1 += 1
#         ptr1 ends at 2 i.e. after 0 point
        
        for i in range(ptr1, len(nums)):
            if nums[i] == 1:
                nums[i], nums[ptr1] = nums[ptr1], nums[i]
                ptr1 += 1
        
        return nums
        
