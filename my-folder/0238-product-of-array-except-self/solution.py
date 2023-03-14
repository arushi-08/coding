class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # left_nums = [1] * len(nums)
        # for i in range(1,len(nums)):
        #     left_nums[i] *= left_nums[i-1] * nums[i-1]

        # right_nums = [1] * len(nums)
        # for i in range(len(nums)-2, -1, -1):
        #     right_nums[i] *= right_nums[i+1] * nums[i+1]
        
        # output_nums = []
        # for i in range(len(nums)):
        #     output_nums.append(left_nums[i] * right_nums[i])
        
        # return output_nums

        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] *= output[i-1] * nums[i-1]

        R = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * R
            R *= nums[i]

        return output

