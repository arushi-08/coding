class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        duplicate_check = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[duplicate_check]:
                duplicate_check += 1
                nums[duplicate_check] = nums[i]
            
        return duplicate_check + 1
