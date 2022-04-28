class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return [-1, -1]
        
        
#         nums.sort()
#         left = 0
#         right = len(nums) - 1
#         while (left < right):
            
#             s = nums[left] + nums[right]
#             if s < target:
#                 left += 1
#             elif s > target:
#                 right -= 1
            
#             else:
#                 return [left, right]
        
#         return [-1, -1]
            
        
