class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 2
        j = 2
        while j < len(nums):
            if nums[j] == nums[i-2]:
                j += 1
                continue
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i
