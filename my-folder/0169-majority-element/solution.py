class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj = nums[0]
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == maj:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    maj = nums[i]
                    counter += 1
        
        return maj
