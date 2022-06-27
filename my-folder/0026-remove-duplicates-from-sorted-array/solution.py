class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[j -1]:
                # print("enter", j)
                i += 1
                # print(i)
                nums[i] = nums[j]
            j += 1
        # print(nums)
        return i + 1
