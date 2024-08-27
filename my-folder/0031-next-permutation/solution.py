class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        find the first smaller element from right side
        swap it with the smallest greater element seen till now on right side
        rest write in sorted order
        """
        # return []

        i = len(nums)-2
        pivot = -1
        while i >= 0:
            if nums[i] < nums[i+1]:
                pivot = i
                break
            i -= 1
        
        if pivot == -1:
            nums.reverse()
            return
        # [1,2,3,2]
        # pivot = 1
        # find the smallest greater element 
        i = pivot + 1
        min_greater_element_idx = pivot + 1
        while i < len(nums):
            if nums[i] > nums[pivot] and nums[min_greater_element_idx] >= nums[i]:
                min_greater_element_idx = i
            i += 1
        
        nums[pivot], nums[min_greater_element_idx] = nums[min_greater_element_idx], nums[pivot]

        left = pivot + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        




        
        

