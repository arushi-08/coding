class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1

        while i > 0:
            if nums[i] > nums[i-1]:
                break
            else:
                i -= 1
        if i == 0:
            # all decreasing
            nums.reverse()
            return
        
        # if i == len(nums) - 1:
        #     nums[i], nums[0] = nums[0], nums[i]
        #     j,k = 1,len(nums)-1
        #     while j<k:
        #         nums[j],nums[k] = nums[k], nums[j]
        #         j += 1
        #         k -= 1

        #     return

        j = i
        # swap i-1 with j
        first_greater_elem = 100
        first_greater_elem_idx = -1
        while j < len(nums):
            if nums[j] > nums[i-1]:
                first_greater_elem = min(first_greater_elem, nums[j])
                if first_greater_elem == nums[j]:
                    first_greater_elem_idx = j
            j += 1
        # print(first_greater_elem_idx, i-1)
        if first_greater_elem_idx == -1:
            first_greater_elem_idx = i
        nums[first_greater_elem_idx], nums[i-1] = nums[i-1], nums[first_greater_elem_idx]

        k = len(nums)-1
        while i<k:
            nums[i],nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
        return 


