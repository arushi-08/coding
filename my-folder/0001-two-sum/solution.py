class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums.sort()
        # print(nums)
        ptr = len(nums)-1
        ptr1 = 0
        
        for i in range(len(nums)):
            if target - nums[i] in nums[:i] + nums[i+1:]:
                if nums.index(target - nums[i]) == i:
                    return [i, nums.index(target - nums[i], i + 1)]
                return [i, nums.index(target - nums[i])]
        
        # ptr2 = len(nums) - 1
        
        # while(ptr1 != ptr):
        #     if nums[ptr1] + nums[ptr] == target:
        #         print(nums[ptr], ptr)
        #         return [ptr1, ptr]
        #     elif nums[ptr1] + nums[ptr] > target:
        #         nums[ptr] -= 1
        #     else:
        #         nums[ptr1] += 1
                    
                    
        return [-1,-1]
