from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict1 = Counter(nums)

        for i in range(len(nums)):
            if i+1 not in dict1:
                return i+1
        
        return len(nums)+1
            
        

