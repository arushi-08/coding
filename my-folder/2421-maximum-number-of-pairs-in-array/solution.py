from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """freq 
        """
        freq_dict = Counter(nums)
        pair_count = 0
#         10 % 2 = 2
        remain_count = 0
        for key, val in freq_dict.items():
            if val > 1:
                pair_count += val // 2
                remain_count += val % 2
            else:
                remain_count += val
        
        
            
        return [pair_count, remain_count]
        
