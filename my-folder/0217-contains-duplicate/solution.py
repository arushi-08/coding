class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                return True
            else:
                dict1[nums[i]] = 1
        
        return False
