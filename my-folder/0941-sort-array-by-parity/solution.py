class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        return nums
        
