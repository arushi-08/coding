class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        # print(nums)
        end = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if end == -1:
                    end = i+1
                while end < len(nums) and nums[end] == 0:
                    end += 1
                if end == len(nums):
                    break

                nums[i], nums[end] = nums[end], nums[i]
                end += 1
            
        return nums


