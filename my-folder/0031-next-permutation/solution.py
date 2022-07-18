class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==1: return nums
        
        ptr1 = ptr2 = len(nums)-1
#         pick 1st ascending from right, 3 5 
        while ptr1 > 0 and nums[ptr1] <= nums[ptr1 - 1]:
            ptr1 -= 1
        
        ptr1 = ptr1 - 1
#         if all descending
        if ptr1 == -1:
            nums.reverse()
            return
        
        while nums[ptr1] >= nums[ptr2]:
            ptr2 -= 1
        
        nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
        
        l, r = ptr1+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        return
