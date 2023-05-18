class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointers
        # ptr1 and ptr2
        # if ptr1 == next pos, while next pos is same, next pos += 1
        # make ptr1 = next pos element, ptr1 += 1
        ptr1 = 1
        ptr2 = 1
        while ptr2 < len(nums):
            if nums[ptr2] != nums[ptr2-1]:
                nums[ptr1] = nums[ptr2]
                ptr1 += 1
            ptr2 += 1
        return ptr1 
