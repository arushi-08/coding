class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd_i = 1
        even_i = 0
        while even_i < len(nums) and odd_i < len(nums):
            if nums[even_i] & 1 == 1 and nums[odd_i] & 1 == 0:
                nums[even_i], nums[odd_i] = nums[odd_i], nums[even_i]
                even_i += 2
                odd_i += 2
            elif nums[odd_i] & 1 == 1:
                odd_i += 2
            elif nums[even_i] & 1 == 0:
                even_i += 2
        
        return nums
