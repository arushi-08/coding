from collections import Counter, defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """ store sum of digits as key and num as value
        return max sum of num
        """
        if not nums: return -1
        
        freq_dict = defaultdict(list)
        for idx, element in enumerate(nums):
            freq_dict[sum([int(digit) for digit in str(element)])].append(element)
        
        max_sum = 0
        visited = set()
        for key, val in freq_dict.items():
            if len(val) == 2:
                max_sum = max(max_sum, sum(val))
            elif len(val) > 2:
                val.sort()
                max_sum = max(max_sum, sum(val[-2:]))
        
        if max_sum == 0:
            return -1
        return max_sum
            
