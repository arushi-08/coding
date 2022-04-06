class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                dict1[nums[i]] += 1
            else:
                dict1[nums[i]] = 1
        
        for i in dict1.keys():
            if dict1[i] == 1:
                return i
        return -1
