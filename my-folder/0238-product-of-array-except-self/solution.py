class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if set(nums) == set([0]): return nums
        product = 1
        second_product = 1
        for i in range(len(nums)):
            if nums[i] == 0 and second_product == product:
                pass
            else:
                second_product *= nums[i]
            product *= nums[i]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = second_product
            else:
                nums[i] = product//nums[i]

        return nums
