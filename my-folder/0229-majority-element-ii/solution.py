from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
#.         [2,  3,   4,  2,     1,      3] 4/3 = 1
# counter1  1        1   1      
# memory1   2        4   2 
# counter2      1         you know that only 2 elements will be > n/3      
# memory2       3           
        counter1, counter2, memory1, memory2 = 0, 0, 0, 0
    
        for i in range(len(nums)):
            if nums[i] == memory1:
                counter1 += 1
            elif nums[i] == memory2:
                counter2 += 1
            elif counter1 == 0:
                memory1 = nums[i]
                counter1 += 1
            elif counter2 == 0:
                memory2 = nums[i]
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
        
        return [n for n in set((memory1, memory2)) if nums.count(n) > len(nums)/3]
            
