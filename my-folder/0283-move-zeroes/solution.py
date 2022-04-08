class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)-1):
            ptr = i + 1
            if nums[i] == 0:
                while(ptr<len(nums) and nums[ptr]==0):
                    ptr += 1
                if ptr == len(nums):
                    break
                temp = nums[i]
                nums[i] = nums[ptr] 
                nums[ptr] = temp
                # ptr += 1
            # print(nums)
        
        return nums
