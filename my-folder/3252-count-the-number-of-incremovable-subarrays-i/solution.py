class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        # total removable subarrays that leave nums inc order

        # find the number of numbers who are like this
        
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                
                is_incremovable = True
                prev_element = -1

                for k in range(i):
                    if prev_element >= nums[k]:
                        is_incremovable = False
                    prev_element = nums[k]

                for k in range(j+1, len(nums)):
                    if prev_element >= nums[k]:
                        is_incremovable = False
                    prev_element = nums[k]

                count += int(is_incremovable)

        return count





