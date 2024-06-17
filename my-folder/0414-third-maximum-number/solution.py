class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums.sort()
        k = 1
        prevelement = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != prevelement:
                k += 1
                prevelement = nums[i]

            if k == 3:
                return nums[i]
        
        return nums[-1]
        

