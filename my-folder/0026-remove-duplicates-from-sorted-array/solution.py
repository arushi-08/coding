class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1, 1, 2,
        k = len(nums) - 1
        p2 = 1
        prev = 0
        for i in range(1, len(nums)):
            
            if nums[i] != nums[prev]:
                print(nums[i], nums[prev])
                nums[p2] = nums[i]
                prev = p2
                p2 += 1
        
        print(nums, p2)
        return p2
    
#         left = 0
#         right = len(nums) - 1
#         length = 0
        
#         while(left <= right):
#             mid = (left + right) // 2
            
#             if nums[mid] == nums[mid + 1]:
#                 nums = nums[:mid+1] + nums[mid + 2:]
#                 length = len(nums) - 1
                
#             if nums[mid] < 
