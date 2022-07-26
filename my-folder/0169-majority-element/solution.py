class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if not nums: return -1
        counter = 1
        current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == current:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    current = nums[i]
                    counter += 1
        
        if counter > 0:
            return current
        return 0
