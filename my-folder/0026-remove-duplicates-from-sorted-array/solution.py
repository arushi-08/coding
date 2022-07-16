class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    #   0     0  1    1    1 2    2  3     3  4
    #   0     1  1    1.   1 2
        if not nums: return 0
        i = 1
        insert_index = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
            else:
                nums[insert_index] = nums[i]
                insert_index += 1
                i += 1
         
        return insert_index
