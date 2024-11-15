import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        def coprime(a, b):
            return math.gcd(a, b)==1
            
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if coprime(int(str(nums[i])[0]), int(str(nums[j])[-1])):
                    count += 1
        
        return count
        
