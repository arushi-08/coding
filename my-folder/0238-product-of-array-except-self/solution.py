class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, prod2 = 1, 1
        num_zeros = 0
        for i in range(len(nums)):
            prod *= nums[i]
            if nums[i] == 0:
                num_zeros += 1
                continue
            prod2 *= nums[i]
            
        answer = []
        
        for i in range(len(nums)):
            if num_zeros > 1:
                answer.append(0)
            elif nums[i] == 0:
                answer.append(prod2)
            else:
                answer.append(prod // nums[i])
            
        return answer
